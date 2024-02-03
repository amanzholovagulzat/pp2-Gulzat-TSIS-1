from itertools import permutations
def fpermutation(str):
    permList = permutations(str)
    for perm in list(permList):
        print(''.join(perm))
str = input()
fpermutation(str)