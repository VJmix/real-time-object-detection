# Real-Time Object Detection algorithm and Program (YOLO)

## Step 1:
 Download the files from Github
  ```
  git clone https://github.com/VJmix/real-time-object-detection.git
  ```
## Step 2:
 Install the basic files: python3, pip3
  ```
  sudo apt-get install python3
  sudo apt-get install python3-pip
  ```
## Step 3:
 Install all the additional packages to run the program:
 OpenCV, imutils, numpy and request 
  ```
  pip3 install imutils
  pip3 install opencv-python
  pip3 install numpy
  pip3 install request
  ```
 OR

  Install all the packages using the requirements file
  ```
  pip3 install -r requirements.txt
  ```
## Step 4:
 Run the code
  ```
  python3 real_time_object_detection.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel --source webcam
  ```
There you go. You will get a window with Yolo running in real time.

If there is a problem, contact me.

https://www.vijaykvganaraju.com/contact

