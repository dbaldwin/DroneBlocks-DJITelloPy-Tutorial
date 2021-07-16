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

db_tello.tt_clear_display()