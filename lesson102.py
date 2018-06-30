# datetime

import datetime

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%Y-%m-%d'))


today = datetime.date.today()
print(today)

import time

print('####')
time.sleep(3)
print('fin')

import os
import shutil

file_name = 'test102.txt'

if os.path.exists(file_name):
    shutil.copy(file_name, '{}_{}'.format(now.strftime('%Y%m%d'), file_name))

with open(file_name, 'w') as f:
    f.write('test')