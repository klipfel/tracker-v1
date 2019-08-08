#!/usr/bin/env python3

"""
Node of the motor driver.
"""

import rospy
from hardware import * # library for the servomotor and the motor.


def main():
    # Node initialization.
    rospy.init_node('motor', log_level=rospy.DEBUG)
    rospy.loginfo("Motor node initialized.")
    # Process.
    global motor
    motor = Motor()
    #motor.terminal_test()  # just for test.
    motor.set_speed(motor.forwardMin)
    #rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
