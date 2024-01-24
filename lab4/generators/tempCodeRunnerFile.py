def generator(x,y):
    for i in range(x,y):
        yield i**2


a = int(input())
b = int(input())
for x in generator(a, b):
    print (x)
