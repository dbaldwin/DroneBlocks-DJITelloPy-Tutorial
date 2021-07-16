from djitellopy import Tello
from DroneBlocksTello import DroneBlocksTello
import time
import random

print("Create Tello object")
tello = Tello()
db_tello = DroneBlocksTello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

for _ in range(0,10):
    tello.send_command_with_return(f"EXT led {random.randint(1,255)} {random.randint(1,255)} {random.randint(1,255)}")
    time.sleep(2)

tello.send_command_with_return("EXT led br 1 100 100 255")
time.sleep(3)
db_tello.tt_set_led_color(random.randint(1,255), random.randint(1,255), random.randint(1,255), freq=1.3)


