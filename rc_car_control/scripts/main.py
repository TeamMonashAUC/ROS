#!/usr/bin/env python
import numpy as np
import rospy
from time import sleep
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

threshold = 1
velocity = 1
pub_joint1 = rospy.Publisher('/rc_car/left_front_wheel_position_controller/command', Float64, queue_size=10)
pub_joint2 = rospy.Publisher('/rc_car/left_rear_wheel_position_controller/command', Float64, queue_size=10)
pub_joint3 = rospy.Publisher('/rc_car/right_front_position_controller/command', Float64, queue_size=10)
pub_joint4 = rospy.Publisher('/rc_car/right_rear_position_controller/command', Float64, queue_size=10)
pub_joint5 = rospy.Publisher('/rc_car/left_steering_hinge_position_controller/command', Float64, queue_size=10)
pub_joint6 = rospy.Publisher('/rc_car/right_steering_hinge_position_controller/command', Float64, queue_size=10)


def findAngle(msg, threshold):
    npArray = np.array([x for x in msg.ranges if (~np.isnan(x) and x > 0)])
    ranges_below_threshold = np.where(npArray <  threshold)[0]
    dir_ranges_below_threshold = (ranges_below_threshold - 540) / 1080.0 * 270
    return dir_ranges_below_threshold
def callback(msg):

    dir_ranges_below_threshold = findAngle(msg, threshold)
    rangeSet1 = set(np.arange(-130.0,-120.0,0.25))
    rangeSet2 = set(np.arange(-83.75, -74.75, 0.5))
    angleSet = set(dir_ranges_below_threshold)
    global velocity
    #if rangeSet1.issubset(angleSet) or rangeSet2.issubset(angleSet):
    #	velocity = -velocity

    rospy.loginfo(dir_ranges_below_threshold)
    #pub_joint5.publish(1)
    #pub_joint6.publish(1)
    #pub_joint1.publish(velocity)
    pub_joint2.publish(velocity)
    #pub_joint3.publish(velocity)
    pub_joint4.publish(velocity)
    #print("min: %f\n" % (min(msg.ranges)))
    #print("max: %f\n" % (max(msg.ranges)))

rospy.init_node('Hokuyo')
sub = rospy.Subscriber('/rc_car_simulation/laser/scan', LaserScan, callback)
rospy.spin()

