#! /usr/bin/env python

import numpy as np
import rospy
from sensor_msgs.msg import LaserScan

threshold = 2

def findAngle(msg, threshold):
    npArray = np.array(msg.ranges)
    ranges_above_threshold = np.where(npArray <  threshold)[0]
    #print(ranges_above_threshold)
    dir_ranges_above_threshold = (ranges_above_threshold - 540) / 1080.0 * 270
    return dir_ranges_above_threshold
def callback(msg):
    dir_ranges_above_threshold = findAngle(msg, threshold)
    print(dir_ranges_above_threshold)
    #print("min: %f\n" % (min(msg.ranges)))
    #print("max: %f\n" % (max(msg.ranges)))
rospy.init_node('Hokuyo')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()


