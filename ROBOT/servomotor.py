#!/usr/bin/env python3

"""
Node of the servomotor driver.
"""

import rospy
from std_msgs.msg import Float64
from hardware import * # library for the servomotor and the motor.

def callback(msg):
	# set the new command for the servomotor.
	rospy.loginfo("[" + rospy.get_caller_id() + "] Command applied : " + str(msg.data))
	servomotor.set_bearing(msg.data)

def main():
    # Node initialization.
    rospy.init_node('servomotor', log_level=rospy.DEBUG)
    rospy.loginfo("Servomotor node initialized.")
    # Process.
    global servomotor
    servomotor = Servomotor()
    # Subscriber.
    sub = rospy.Subscriber("bearing/command",Float64, callback)
    # Spinning.
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
