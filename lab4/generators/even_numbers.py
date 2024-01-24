def generator(N):
    for i in range(N): 
        if (i % 2) == 0:
            yield i

a = int(input())
list1 = list()
for x in generator(a):
    list1.append(str(x))
print(', '.join(list1))