# Robust Deep Learning Tracking Robot - prototype v1

## What can you find here?

This README file gives the necessary steps to reproduce the latest results of the tracker. More precisely, this github repository implements a version of the tracker, where the Jetson Nano sends the information (frames ..) to a remote computer before processing on the remote computer. The processing of the tracking algorithm Goturn was tested on the Jetson Nano, but with poor performances (1-3 FPS). Which explains the choice of the remote processing.

The control of the speed with the depth information of the stereo camera was not implemented here. The speed is fixed manually to the minimum.

The robot was tested with an Ethernet cable, since the wifi dongle had some driver issues. Adding the  wifi module of Intel AC 8625 and the Chaogang antennas 648109 is recommended to benefit from the best processing speed.

This repository propose the raw codes, and not a ROS workspace or package to avoid any dependency issue.

Attention : this code was calibrated with the hardware of the robot, which is not disclosed in this  github (refer to the report).

## Setup

### Remote Computer

The remote computer used for the test was an ASUS G703VI. The hardware of the computer will influence the performances of the tracking : 5-6 FPS reached.

#### Dependencies

* Ubuntu 18.04 bionic

* ROS melodic : [ROS wiki](http://wiki.ros.org/melodic/Installation/Ubuntu).

  * Check that  the `cv_bridge`  is installed : 

  ```bash
  rospack list | grep cv_bridge
  ```

  If nothing outputs, install the package with the following command: ([ROS package](http://wiki.ros.org/vision_opencv))

  ```bash
  sudo apt install ros-melodic-vision-opencv
  ```

* Create a ROS workspace: [ROS tutorial](http://wiki.ros.org/catkin/Tutorials/create_a_workspace).

* Create the package `remote_tracker`: 

```bash
catkin_create_pkg remote_tracker sensor_msgs cv_bridge rospy std_msgs
```

* Virtual environment with opencv > 3.4.2: the tracking algorithm *Goturn* requires a specific opencv version.

```bash
virtualenv --version  # checking if you already have it installed.
# In case you do not have it : installation.
sudo apt-get update
sudo apt-get install python-virtualenv
# Setting up the python environment.
virtualenv --system-site-packages -p python2.7 ~/opencv_py_env
source ~/opencv_py_env/bin/activate
pip install numpy
pip install -U rosinstall msgpack empy defusedxml netifaces
python -V
pip install opencv-contrib-python
deactivate
```

The interpreter of the `opencv_py_env` is then specified in the first line of the `tracker.py` file.

* In the `tracker.py` change the first line specifying the interpreter of the `opencv_py_env`: you need to replace `arnaud` by your username.
* Place the code inside the folder `remote` into the ROS package `remote_tracker`. 

### Robot

Make sure that the hardware of the robot is installed as presented in the hardware architecture of the report.

For the software:

* Download the Jetson Nano image ([official link](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#write)).
* ROS melodic.
* ROS workspace.
* Create the ROS package `robot_tracker` : follow the same steps as above.
* Place the codes inside the `robot` folder in the ROS package `robot_tracker`.

### Network

* Connect the remote computer to a network through Wifi or Ethernet, and connect the Jetson Nano to the same network through Ethernet or with a Wifi dongle that tested beforehand. The bandwidth will directly impact the tracking rate.

## Launching

