from djitellopy import Tello
import time

if __name__ == '__main__':
    speed = 30
    time_in_seconds = 3
    
    print("Create Tello object")
    tello = Tello()
    
    print("Connect to Tello Drone")
    tello.connect()
    
    battery_level = tello.get_battery()
    print(f"Battery Life Percentage: {battery_level}")
    
    print("Takeoff!")
    tello.takeoff()
    
    # send_rc_control(left_right_velocity, foward_backward_velocity, up_down_velocity, yaw_velocity)
    # left_right_velocity: -100~100(left / right)
    # forward_backward_velocity: -100~100( backward / forward )
    # up_down_velocity: -100~100( down / up )
    # yaw_velocity: -100~100 (Counter Clockwise, Clockwise )
    
    print("Left")
    tello.send_rc_control(-speed, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 4 seconds")
    time.sleep(4)
    
    print("Stop")
    tello.send_rc_control(0, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 1/2 seconds")
    time.sleep(0.5)
    
    print("Right")
    tello.send_rc_control(speed, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 4 seconds")
    time.sleep(4)
    
    print("Stop")
    tello.send_rc_control(0, 0, 0, 0)
    print("Return from send_rc_control")
    print("Sleep 1/2 seconds")
    time.sleep(0.5)
    
    print("Up")
    tello.send_rc_control(0, 0, speed, 0)
    print("Return from send_rc_control")
    print(f"Sleep {time_in_seconds} seconds")
    time.sleep(time_in_seconds)
    
    print("Down")
    tello.send_rc_control(0, 0, -speed, 0)
    print("Return from send_rc_control")
    print(f"Sleep {time_in_seconds} seconds")
    time.sleep(time_in_seconds)
    
    print("Forward")
    tello.send_rc_control(0, speed, 0, 0)
    print("Return from send_rc_control")
    print(f"Sleep {time_in_seconds} seconds")
    time.sleep(time_in_seconds)
    
    print("Backwards")
    tello.send_rc_control(0, -speed, 0, 0)
    print("Return from send_rc_control")
    print(f"Sleep {time_in_seconds} seconds")
    time.sleep(time_in_seconds)
    
    print("Clockwise")
    tello.send_rc_control(0, 0, 0, speed)
    print("Return from send_rc_control")
    print(f"Sleep {time_in_seconds} seconds")
    time.sleep(time_in_seconds)
    
    print("Counter Clockwise")
    tello.send_rc_control(0, 0, 0, -speed)
    print("Return from send_rc_control")
    print(f"Sleep {time_in_seconds} seconds")
    time.sleep(time_in_seconds)
    
    tello.send_rc_control(0, 0, 0, 0)
    time.sleep(0.5)
    
    print("landing")
    tello.land()
    print("touchdown.... goodbye")
