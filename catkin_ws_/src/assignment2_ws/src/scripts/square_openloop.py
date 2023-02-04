#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
PI = 3.1415926535897

def move():
    # Starts a new node
    rospy.init_node('square_openloop', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    speed = 0.2
    distance = 2
    angular_vel = 0.2
    relative_angle = 90*2*PI/360
    
    #Since we are moving just in x-axis
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    
    i = 1
    
    while not rospy.is_shutdown() and i < 5:

        #Setting the current time for distance calculus
        
        current_distance = 0
        current_angle = 0
        rospy.Time(secs=0, nsecs=0)
        t0 = rospy.Time.now().to_sec()
        #Loop to move the turtle in an specified distance
        while(current_distance < distance):
            vel_msg.linear.x = speed
            vel_msg.angular.z = 0
            velocity_publisher.publish(vel_msg)
            t1=rospy.Time.now().to_sec()
            current_distance = speed*(t1-t0)
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)
        
        rospy.Time(secs=0, nsecs=0)
        t2 = rospy.Time.now().to_sec()
        
        while(current_angle < relative_angle):
            vel_msg.angular.z = angular_vel
            vel_msg.linear.x = 0     
            velocity_publisher.publish(vel_msg)
            t3 = rospy.Time.now().to_sec()
            current_angle = angular_vel*(t3-t2)
        vel_msg.angular.z = 0
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)
        i += 1
        
    rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        move()
    except rospy.ROSInterruptException: pass
