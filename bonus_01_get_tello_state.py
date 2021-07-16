from djitellopy import Tello
import time
from pprint import pprint


print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

print("Takeoff!")
tello.takeoff()

print("Get entire Tello Current State")
# {'pitch': 0, 'roll': 0, 'yaw': 29, 'vgx': 0, 'vgy': 0, 'vgz': 0, 'templ': 76, 'temph': 78, 'tof': 72, 'h': -10, 'bat': 67, 'baro': 235.23, 'time': 38, 'agx': -22.0, 'agy': -15.0, 'agz': -1059.0}
tello_state = tello.get_current_state()
print(tello_state)

for i in range(0,10):
    print("----------- New State Record -------")
    tello_state = tello.get_current_state()
    pprint(tello_state, indent=2)
    time.sleep(1)

print("landing")
tello.land()
print("touchdown.... goodbye")
