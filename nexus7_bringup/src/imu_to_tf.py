#!/usr/bin/env python  
import roslib
roslib.load_manifest('nexus7_bringup')
import rospy

import tf
from sensor_msgs.msg import Imu

def handle_imu(msg):
    br = tf.TransformBroadcaster()
    br.sendTransform((0, 0, 0),
                     (msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w),
                     rospy.Time.now(),
                     "base_link",
                     "imu")

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    rospy.Subscriber('/android/imu', Imu, handle_imu)
    rospy.spin()