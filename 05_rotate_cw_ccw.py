from djitellopy import Tello
import time

if __name__ == '__main__':

    print("Create Tello object")
    tello = Tello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Takeoff!")
    tello.takeoff()

    print("Rotate Clockwise")
    tello.rotate_clockwise(90)

    time.sleep(1)

    print("Rotate Counter Clockwise")
    tello.rotate_counter_clockwise(90)

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
