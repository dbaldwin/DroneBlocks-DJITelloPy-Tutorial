from djitellopy import Tello

if __name__ == '__main__':

    print("Create Tello object")
    tello = Tello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Takeoff!")
    tello.takeoff()

    print("Move Up")
    tello.move_up(40)

    print("Move Down")
    tello.move_down(40)

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
