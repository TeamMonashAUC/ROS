#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

pub_joint1 = rospy.Publisher('/rc_car/left_front_wheel_position_controller/command', Float64, queue_size=10)
pub_joint2 = rospy.Publisher('/rc_car/left_rear_wheel_position_controller/command', Float64, queue_size=10)
pub_joint3 = rospy.Publisher('/rc_car/right_front_position_controller/command', Float64, queue_size=10)
pub_joint4 = rospy.Publisher('/rc_car/right_rear_position_controller/command', Float64, queue_size=10)
pub_joint5 = rospy.Publisher('/rc_car/left_steering_hinge_position_controller/command', Float64, queue_size=10)
pub_joint6 = rospy.Publisher('/rc_car/right_steering_hinge_position_controller/command', Float64, queue_size=10)

def callback(data):
    speed = data.linear.x
    angle = data.angular.z
    rospy.loginfo(speed)
    rospy.loginfo(angle)
    pub_joint1.publish(speed)
    pub_joint3.publish(speed)
    pub_joint2.publish(speed)
    pub_joint4.publish(speed)
    pub_joint5.publish(angle)
    pub_joint6.publish(angle)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/cmd_vel", Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
