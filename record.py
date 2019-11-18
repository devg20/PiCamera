#Open Thonny IDE in RaspberryPi and run the following code to capture a photo using the RaspberryPI Camera Module

from picamera import PiCamera         #Importing required libraries
from time import sleep
from subprocess import call           #For video format conversion

camera=PiCamera()                     #Creating a varible to use Picamera functions
print("Preview Started.")   
camera.start_preview()                #Inorder to give the camera some time to focus
camera.sleep(5)                       #5 seconds preview time
camera.stop_preview()
print("Recoding started")
camera.start_recording("video.h264")  #Recoding started
sleep(10)
camera.stop_recording()               #Video recorded
print("Video recorded")

#To convert the video into mp4 
command=("MP4Box -add video.h264 convertedvideo.mp4")
call([command], shell=True)           #Using the call function

