import datetime

datetime_now = datetime.datetime.now()
print(datetime_now)

datetime_today = datetime.datetime.today()
print(datetime_today)

print('datetime_today.day=>',datetime_today.day)
print('datetime_today.month=>',datetime_today.month)
print('datetime_today.year=>',datetime_today.year)

d = datetime.date(2019, 4, 13)
print('d=>',d)