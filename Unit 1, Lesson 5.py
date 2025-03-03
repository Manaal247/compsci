import math
print ("Area of a norman window calculator")
radius = input("please input a radius: ")
radius = float(radius)
rad = math.pow(radius, 2)
area = 0.5*math.pi*rad
area1 = 4*rad
totalarea = area + area1
print ("The dimensions of the norman window are", totalarea)
