from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta
print(datetime.strptime('2023-04-26', '%Y-%m-%d').date())
print(date.today().day)
to_date = str(date.today() - timedelta(days=1)) if date.today().day != 1 else str(date.today())
print(to_date)