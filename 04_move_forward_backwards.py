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

    print("Move Forward")
    tello.move_forward(40)

    time.sleep(1)

    print("Move Backwards")
    tello.move_back(40)

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
