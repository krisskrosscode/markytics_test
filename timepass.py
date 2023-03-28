from datetime import datetime, date, timedelta

# print(date.today())
# print(datetime.now().date())

# print(datetime.strptime(datetime.now().time().strftime('%H:%M:%S'), '%H:%M:%S'))

b = date.today()
a =(datetime.now() - timedelta(hours=1)).time().strftime('%H:%M')

print(a, b)