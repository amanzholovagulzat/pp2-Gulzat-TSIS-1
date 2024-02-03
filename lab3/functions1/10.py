def func(int):
    list2 = []
    for i in list1:
        for j in list1:
            if j in list2:
                continue
            else:
                list2.append(j)
    print(' '.join(list2))


list1 = list(input().split(' '))
func(list1)
