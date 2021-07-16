from djitellopy import Tello
from DroneBlocksTello import DroneBlocksTello
import time

print("Create Tello object")
tello = Tello()
db_tello = DroneBlocksTello()

print("Connect to Tello Drone")
tello.connect()
# db_tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

tello.send_command_with_return("EXT led 255 0 0")
time.sleep(3)
db_tello.tt_set_led_color(0,255,0)
time.sleep(3)


