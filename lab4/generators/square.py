def generator(N):
    for i in range(N): 
        yield i**2

a = int(input())
for x in generator(a):
    print (x)