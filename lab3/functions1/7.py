def has_33(int):
    bool = True
    for i in list1:
        if i == len(list1):
            break
        if list1[i] == list1[i+1]:
            break
        else: bool = False
    if bool == True: print("True")
    else: print("False")


list1 = list(map(int, input().split(' ')))
has_33(list1)
