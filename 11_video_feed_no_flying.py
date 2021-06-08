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

# read a single image from the Tello video feed
print("Read Tello Image")
frame_read = tello.get_frame_read()

time.sleep(2)
while True:
    # read a single image from the Tello video feed
    print("Read Tello Image")
    tello_video_image = frame_read.frame

    # use opencv to write image
    if tello_video_image is not None:
        cv2.imshow("TelloVideo", tello_video_image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

tello.streamoff()
cv2.destroyWindow('TelloVideo')
cv2.destroyAllWindows()
