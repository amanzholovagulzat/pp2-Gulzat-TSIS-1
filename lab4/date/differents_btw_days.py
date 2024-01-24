import datetime

def date_diff_in_Seconds(date2, date1):
    x = date2 - date1
    return x.days * 24 * 3600 + x.seconds


list = input().split('-')
for i in range(3):
    if i == 0:
        a = int(list[i])
    elif i == 1:
        b = int(list[i])
    elif i == 2:
        c = int(list [i])

date1 = datetime.datetime(a, b, c)

list1 = input().split('-')
for i in range(3):
    if i == 0:
        a1 = int(list1[i])
    elif i == 1:
        b1 = int(list1[i])
    elif i == 2:
        c1 = int(list1[i])

date2 = datetime.datetime(a1, b1, c1)

print("%d seconds" %(date_diff_in_Seconds(date2, date1)))