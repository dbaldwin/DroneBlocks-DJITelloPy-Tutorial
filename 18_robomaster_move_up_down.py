from DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':

    print("Create Tello object")
    tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    tello.connect()

    print("Clear display")
    tello.clear_display()


    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Takeoff!")
    tello.takeoff()

    print("Move Up")
    tello.display_up_arrow()
    tello.move_up(40)

    tello.display_heart()
    time.sleep(3)

    print("Move Down")
    tello.display_down_arrow()
    tello.move_down(40)

    tello.display_smile()
    time.sleep(3)

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
    tello.clear_display()
