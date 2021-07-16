# DroneBlocks DJITelloPy API Tutorial

This course will take a deep dive into the DJITelloPy Python API and how a python program communicates to the Tello drone.  We will look at a number of the methods available to control the Tello drone from any Python script.  In addition you can use the commands you learn in this course, in the other courses on Advanced Tello Programming with Python.  By the end of this course you will know how to install the necessary libraries, and create Python scripts to interact with the Tello drone.  With these building blocks, you create your own scripts to customize the flying pattern of the Tello drone.
The repository contains the scripts for the DroneBlocks Tutorial that covers the DJITelloPy Python API.

## Setup

### Step 1 - Download the source code zip file

Download the zip for for this course.  If you are familiar with 'Git', you can also clone this repository

Unzip the download and move the folder where you would like to keep the project source code.

### Step 2 - Create a python virtual environment

Open a terminal window and change directory to where you saved the folder from above.

Check your python version by typing both commands below to determine which python installation is Python 3.6 or higher.

```shell
python --version
python3 --version
```

Choose either 'python' or 'python3' - whichever returned a python version greater than 3.6.


Inside the project folder, type the following:

```shell
python3 -m venv venv
```

### Activate Virtual Environment

*VERY IMPORTANT*

Activate the newly created python virtual environment so all of the libraries are install into the project and not the global Python installation.

This will help keep this projects libraries out of other projects.

* MacOS
```shell
source venv/bin/activate
```

* Windows
```shell
.\venv\Scripts\activate
```

### Install Libraries

In the same terminal window type:

```shell
pip install -r requirements.txt
```

This will install all of the necessary libraries for this project.

### Test the Installation

```shell
python 00_test_installation.py
```

In the terminal you should see the message: 

```shell
Your installation worked!
```

## DJI Tello SDK Documentation
Below are links to the official DJI Tello SDK documentation.  These documents will provide the detail of all of the commands that the Tello can accept.


### Version 2.0

[V2.0 Tello SDK](https://dl-cdn.ryzerobotics.com/downloads/Tello/Tello%20SDK%202.0%20User%20Guide.pdf)

### Version 3.0

[V3.0 Tello SDK](https://dl.djicdn.com/downloads/RoboMaster+TT/Tello_SDK_3.0_User_Guide_en.pdf)


## Resources

Great article on the difference between [Pitch, Roll, Yaw](https://emissarydrones.com/what-is-roll-pitch-and-yaw).
