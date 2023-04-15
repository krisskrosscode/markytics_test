from datetime import datetime


with open('test_log.txt', 'a+') as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')