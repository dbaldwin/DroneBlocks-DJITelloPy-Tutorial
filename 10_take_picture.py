from djitellopy import Tello
import cv2
import time

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

time.sleep(2)

print("Turn Video Stream On")
tello.streamon()

frame_read = tello.get_frame_read()

print("Takeoff!")
tello.takeoff()

print("I will take a picture in 2 seconds")
time.sleep(1)
print("I will take a picture in 1 seconds")
time.sleep(1)

# read a single image from the Tello video feed
print("Read Tello Image")
tello_video_image = frame_read.frame

print("Write tello-picture.png")
# use opencv to write image
cv2.imwrite("tello-picture.png", tello_video_image)

print("Land")
tello.land()

print("Turn Tello video stream off")
tello.streamoff()
