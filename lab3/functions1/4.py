def filter_prime(x):
    prime = True
    if x == 1: prime = False
    for i in range(2, x):
        if x % i == 0:
            prime = False
    if prime == True:
        print(x, sep=' ')
list1 = list(map(int, input().split(' ')))
for i in range(len(list1)):
    filter_prime(list1[i])