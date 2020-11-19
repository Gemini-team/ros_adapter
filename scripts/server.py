#!/usr/bin/env python2

from concurrent import futures
import logging

import rospy
import std_msgs.msg
from std_msgs.msg import String, Header
from sensor_msgs.msg import Image
from sensor_msgs.msg import PointCloud2

from cv_bridge import CvBridge, CvBridgeError

import grpc
import cv2

from sensor_streaming import sensor_streaming_pb2
from sensor_streaming import sensor_streaming_pb2_grpc

import numpy as np


class SensorStreaming(sensor_streaming_pb2_grpc.SensorStreamingServicer):
    def __init__(self, camera_pub, lidar_pub):
        print("creating")
        self.bridge = CvBridge()
        self.camera_pub = camera_pub
        self.lidar_pub = lidar_pub

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

        self.camera_pub.publish(msg)

        return sensor_streaming_pb2.CameraStreamingResponse(success=True)

    def StreamLidarSensor(self, request, context):
        lidarfields = request.LidarFields
    
        pointcloud_msg = PointCloud2()
        header = std_msgs.msg.Header()
        header.stamp = request.timeInSeconds


        header.frame_id = "lidar"
        pointcloud_msg.header = header
        
        print(pointcloud_msg)

#        pointcloud_msg.height = request.height
#        pointcloud_msg.width = request.width
#
#        pointcloud_msg.is_bigendian = request.isBigEndian
#        pointcloud_msg.point_step = request.point_step
#        pointcloud_msg.row_step = request.row_step
#        pointcloud_msg.data = request.data
#        pointcloud_msg.is_dense = request.isDense
#
#        print(pointcloud_msg)

        return sensor_streaming_pb2.LidarStreamingResponse(success=True)


def serve(camera_pub, lidar_pub):
    ip = '192.168.0.116'
    port = '30052'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    sensor_streaming_pb2_grpc.add_SensorStreamingServicer_to_server(SensorStreaming(camera_pub, lidar_pub), server)
    server.add_insecure_port(ip + ':' + port)
    print(ip + ":" + port)
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    camera_pub = rospy.Publisher('server_image', Image, queue_size=10)
    lidar_pub = rospy.Publisher('server_lidar', PointCloud2, queue_size=10)
    rospy.init_node('server', anonymous=True)
    serve(camera_pub, lidar_pub)