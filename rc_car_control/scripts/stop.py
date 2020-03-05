#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64

def talker():
	pub_joint1 = rospy.Publisher('/rc_car/joint1_position_controller/command', Float64, queue_size=10)
	pub_joint2 = rospy.Publisher('/rc_car/joint2_position_controller/command', Float64, queue_size=10)
	pub_joint3 = rospy.Publisher('/rc_car/joint3_position_controller/command', Float64, queue_size=10)
	pub_joint4 = rospy.Publisher('/rc_car/joint4_position_controller/command', Float64, queue_size=10)
	rospy.init_node('rc_stopper', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub_joint1.publish(0)
		pub_joint2.publish(0)
		pub_joint3.publish(0)
		pub_joint4.publish(0)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

