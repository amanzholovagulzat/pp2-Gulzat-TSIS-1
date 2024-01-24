import datetime

today = datetime.datetime.now()
yesterday = today.day - 1
tomorrow = today.day + 1
print("Yesterday:", datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second))
print("Today:", datetime.datetime(today.year, today.month, yesterday, today.hour, today.minute, today.second))
print("Tomorrow:", datetime.datetime(today.year, today.month, tomorrow, today.hour, today.minute, today.second))