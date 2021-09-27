from DroneBlocksTello import DroneBlocksTello
import time

if __name__ == '__main__':
    print("Create Tello object")
    db_tello = DroneBlocksTello()

    print("Connect to Tello Drone")
    db_tello.connect()

    battery_level = db_tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Set LED to Red")
    db_tello.send_command_with_return("EXT led 255 0 0")
    time.sleep(3)

    print("Set LED to Green")
    db_tello.tt_set_led_color(0,255,0)
    time.sleep(3)



