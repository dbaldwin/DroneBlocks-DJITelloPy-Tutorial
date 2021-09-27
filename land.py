from djitellopy import Tello

if __name__ == '__main__':

    print("Create Tello object")
    tello = Tello()

    print("Connect to Tello Drone")
    tello.connect()

    print("landing")
    tello.land()
    print("touchdown.... goodbye")
