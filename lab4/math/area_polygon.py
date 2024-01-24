import math

def ctg(value):
    return 1 / math.tan(radian)

n = float(input("Input number of sides: "))
a = float(input("Input the length of a side: "))

grad = 180/n
radian = grad*(math.pi/180)
cot = ctg(radian)

S = int((n * pow(a, 2) * cot)/4)
print("The area of the polygon is:", S)