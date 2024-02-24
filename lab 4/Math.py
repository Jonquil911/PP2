import math

#ex1
print("Output radian:", math.radians(float(input("Input degree: "))))

#ex2
height, base1, base2 = float(input("Height: ")), float(input("Base, first value: ")), float(input("Base, second value: "))
print("Expected Output:", height * (base1 + base2)/2)

#ex3
sides, length = float(input("Input number of sides: ")), float(input("Input the length of a side: "))
print("The area of the polygon is: ", ((sides/4)*pow(length,2)*(1/math.tan(math.pi/sides))))

#ex4
base, height = float(input("Length of base: ")), float(input("Height of parallelogram: "))
print("Expected Output: ", float(base*height))