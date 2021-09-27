from djitellopy import Tello
import time

if __name__ == '__main__':
    travel_distance_cm = 50
    speed = 20

    print("Create Tello object")
    tello = Tello()

    print("Connect to Tello Drone")
    tello.connect()

    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")

    print("Takeoff!")
    tello.takeoff()

    time.sleep(1)

    """
    Flight Patter
        2     4
        |\   /|
        | \ / |
        |  \  |
        | / \ |
       1 5   3
    
    """

    #tello.go_xyz_speed(x,y,z, speed)

    # x - (+)foward/(-)backwards
    # y - (+)left/(-)right
    # z - (+)up/(-)down
    tello.go_xyz_speed(0, 0, travel_distance_cm, speed)
    print("sleep")
    time.sleep(0.5)
    tello.go_xyz_speed(0, travel_distance_cm, -travel_distance_cm, speed)
    print("sleep")
    time.sleep(0.5)
    tello.go_xyz_speed(0, 0, travel_distance_cm, speed)
    print("sleep")
    time.sleep(0.5)

    # x - (+)foward/(-)backwards
    # y - (+)left/(-)right
    # z - (+)up/(-)down
    tello.go_xyz_speed(0, -travel_distance_cm, -travel_distance_cm, speed)
    print("sleep")
    time.sleep(0.5)

    print("landing")
    tello.land()
    print("touchdown.... goodbye")

