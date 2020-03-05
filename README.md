# ROS
src folder of catkin workspace of jetson nano

These files are the packages created by members from Electrical/Intelligence Department of Shell Eco Marathon Team Monash.

Autonomous rc car driving involves 4 steps:
1. Mapping
2. Localisation
3. Path Planning
4. Motor Control

This repository provides the launch files and python scripts for the 4 steps mentioned above. Step 3, Path Planning is not properly tested yet. In additon, step 4, Motor control is not done yet but the concept is by running move_base.launch in rc_car_nav package, it will publish velocity message(linear and angular) about the car in rviz to a topic called /cmd_vel. Then, we need to create a package and launch file to subscribe to /cmd_vel to obtain the velocities and send serial message to arduino so that arduino as a microcontroller can control the speed of dc motor and position of servo motor based on the serial message.
