import math

radius = input("Enter the radius of the sphere in ft: ")

o_x = 0
o_y = 0
o_z = radius

theta = math.radians(float(input("Choose the angle on the xy plane the ring will face (degrees): ")))
phi = math.radians(float(input("Choose the angle from the horizontal that the ring will face: ")))

print(theta, phi)

n_x = int(radius) * math.sin(phi) * math.cos(theta)
n_y = int(radius) * math.sin(phi) * math.sin(theta)
n_z = int(radius) * math.cos(phi)

# print(n_x, n_y, n_z)

del_x = n_x
del_y = n_y
del_z = n_z - int(o_z)

del_xy = math.sqrt((del_x * del_x) + (del_y * del_y))

print("The total xy distance from the center is " + str(del_xy) + " ft or " + str(del_xy * 12) + " in")

del_xyz = math.sqrt((del_x * del_x) + (del_y * del_y) + (del_z * del_z))

print(f"The total displacement of the center of the ring is {del_xyz} ft or {12 * del_xyz} in")
