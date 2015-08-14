import datetime

today = datetime.datetime.now()
print 'Today    :', today

one_day = datetime.timedelta(days=10, hours=5, minutes=10, seconds=29)
print 'One day  :', one_day

yesterday = today - one_day
print 'Yesterday:', yesterday


print(yesterday.strftime('%y'))
print(yesterday.strftime('%m'))
print(yesterday.strftime('%d'))
print(yesterday.strftime('%H'))
print(yesterday.strftime('%M'))
print(yesterday.strftime('%S'))


