def down_to_0(N):
    for i in range(N,0,-1):
        yield i


n = int(input())
for x in down_to_0(n):
    print(x)