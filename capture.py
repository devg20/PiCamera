-Open Thonny IDE in RaspberryPi and run the following code to capture a photo using the RaspberryPI Camera Module

from picamera import PiCamera //Importing required libraries
from time import sleep

camera=PiCamera()             //Creating a varible to use Picamera functions
print("Preview Started.")   
camera.start_preview()        //Inorder to give the camera some time to focus
camera.sleep(5)               //5 seconds preview time
camera.stop_preview()
print("Capturing Shot")
camera.capture("photo.jpg")   //Capturing picture
print("Picture Captured")


