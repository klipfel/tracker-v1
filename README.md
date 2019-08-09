# Robust Deep Learning Tracking Robot - prototype v1

## What can you find here?

This README file gives the necessary steps to reproduce the latest results of the tracker. More precisely, this github repository implements a version of the tracker, where the Jetson Nano sends the information (frames ..) to a remote computer before processing on the remote computer. The processing of the tracking algorithm Goturn was tested on the Jetson Nano, but with poor performances (1-3 FPS). Which explains the choice of the remote processing.

The control of the speed with the depth information of the stereo camera was not implemented here. The speed is fixed manually to the minimum.

The robot was tested with an Ethernet cable, since the wifi dongle had some driver issues. Adding the  wifi module of Intel AC 8625 and the Chaogang antennas 648109 is recommended to benefit from the best processing speed.

This repository propose the raw codes, and not a ROS workspace or package to avoid any dependency issue.

## Setup

### Remote Computer

The remote computer used for the test was an ASUS G703VI.

#### Dependencies

* Ubuntu 18.04 bionic
* ROS melodic : [ROS wiki](http://wiki.ros.org/melodic/Installation/Ubuntu).
* Creating a ROS workspace: [ROS tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).
* Creating the package `remote_tracker`: 

```bash
catkin_create_pkg remote_tracker sensor_msgs cv_bridge rospy std_msgs
```



* Virtual environment with opencv > 3.4.2

### Robot

* Jetson Nano image ([official link](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)).
* ROS melodic.
* ROS workspace

### Network



## Launching

