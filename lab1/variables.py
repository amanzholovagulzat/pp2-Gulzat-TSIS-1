#1
x = 5
y = "John"
print(x)
print(y)
#2
x = 4
x = "Sally"
print(x)
#3
x = str(3)
y = int(3)
z = float(3)
print(x)
print(y)
print(z)
#4
x = 5
y = "John"
print(type(x))
print(type(y))
#5
x = "John"
print(x)
x = 'John'
print(x)
#6
a = 4
A = "Sally"
print(a)
print(A)
#variable names 1
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#assign multiple values
#1
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#2
x = y = z = "Orange"
print(x)
print(y)
print(z)
#3
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#output variables
#1
x = "Python is awesome"
print(x)
#2
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#3
x = 5
y = 10
print(x + y)
#4
x = 5
y = "John"
print(x, y)
#global variables
#1
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#2
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#3
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#variable exercises
carname = "Volvo"

x = 50

x = 5
y = 10
print(x+y)

x = 5
y = 10
z = x + y
print(z)

myfirst_name = "John"

x = y = z ="Orange"

def myfunc(): 
  global x
  x = "fantastic"