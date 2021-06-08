from djitellopy import Tello

print("Create Tello object")
tello = Tello()

print("Connect to Tello Drone")
tello.connect()

battery_level = tello.get_battery()
print(f"Battery Life Percentage: {battery_level}")

print("Takeoff!")
tello.takeoff()

# tello.go_xyz_speed(x,y,z, speed)
# x - (+)foward/(-)backwards
# y - (+)left/(-)right
# z - (+)up/(-)down

# Forward, Right, Up
print("Go x,y,z: (30,-30,30)")
tello.go_xyz_speed(30,-30,30, 20)

# Note that the DJITelloPy documentation indicates that the values
# x,y,z are between 20-500, the official documentation states the
# valid values are from -500-500
# Backwards, Left, Down
print("Go x,y,z: (-60,60,-60)")
tello.go_xyz_speed(-60,60,-60, 20)

# Forward, Right, Up
print("Go x,y,z: (30,-30,30)")
tello.go_xyz_speed(30,-30,30, 20)


print("landing")
tello.land()
print("touchdown.... goodbye")
