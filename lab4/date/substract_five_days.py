import datetime

substract_d = datetime.datetime.now()
new_day = int(substract_d.day) - 5
q = datetime.datetime(substract_d.year, substract_d.month, new_day, substract_d.hour, substract_d.minute, substract_d.second)
print(q)