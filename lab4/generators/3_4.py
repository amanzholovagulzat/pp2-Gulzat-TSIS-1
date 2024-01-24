def generator(N):
    for i in range(N): 
        if (i % 3) == 0 and (i % 4) == 0:
            yield i

a = int(input())
for x in generator(a):
    print (x)