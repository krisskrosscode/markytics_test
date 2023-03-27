from datetime import datetime, date, time

print(date.today())
print(datetime.now().date())

print(datetime.strptime(datetime.now().time().strftime('%H:%M:%S'), '%H:%M:%S'))