#!/usr/bin/env python2

from concurrent import futures
import logging

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image

from cv_bridge import CvBridge, CvBridgeError

import grpc
import cv2

from sensor_streaming import sensor_streaming_pb2
from sensor_streaming import sensor_streaming_pb2_grpc

import numpy as np

class SensorStreaming(sensor_streaming_pb2_grpc.SensorStreamingServicer):
    def __init__(self, pub):
        print("creating")
        self.bridge = CvBridge()
        self.pub = pub

    def StreamCameraSensor(self, request, context):
        img_string = request.data

        cv_image = np.fromstring(img_string, np.uint8)

        # Backward for some wierd reason
        cv_image = cv_image.reshape(640, 800, 3)
        cv_image = cv2.flip(cv_image, 0)

        msg = 0
        try:
            msg = self.bridge.cv2_to_imgmsg(cv_image, 'rgb8')
        except CvBridgeError as e:
            print(e)

        self.pub.publish(msg)

        return sensor_streaming_pb2.CameraStreamingResponse(success=True)


def serve(pub):
    ip = '192.168.0.116'
    port = '30052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    sensor_streaming_pb2_grpc.add_SensorStreamingServicer_to_server(SensorStreaming(pub), server)
    server.add_insecure_port(ip + ':' + port)
    print(ip + ":" + port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    pub = rospy.Publisher('server_image', Image, queue_size=10)
    rospy.init_node('server', anonymous=True)
    serve(pub)
