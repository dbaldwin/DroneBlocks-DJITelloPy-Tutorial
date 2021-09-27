from DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':

    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    for color in ['red', 'blue', 'purple']:
        db_tello.clear_display()

        # db_tello.display_message("Hello Python class",)

        db_tello.display_up_arrow(color)

        time.sleep(1)

        db_tello.display_down_arrow(color)

        time.sleep(1)

        db_tello.display_left_arrow(color)

        time.sleep(1)

        db_tello.display_right_arrow(color)

        time.sleep(1)

    db_tello.display_heart('red')


