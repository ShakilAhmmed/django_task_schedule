from apscheduler.schedulers.background import BackgroundScheduler

import os
from shutil import copyfile
import datetime
from django.conf import settings


def job_function():
    print("Hello World")


def database_backup():
    print("Getting Backup...")
    dir_data = os.path.join(settings.BASE_DIR, 'backup')
    currentDT = datetime.datetime.now()
    get_date = str(currentDT.year) + '-' + str(currentDT.month) + '-' + str(currentDT.day)
    file_name = f"{get_date}-{currentDT.minute}-database.sqlite3"
    if not os.path.exists(dir_data):
        os.mkdir(dir_data)
    copyfile(os.path.join(settings.BASE_DIR, 'db.sqlite3'), f"{dir_data}/{file_name}")
    print("Getting Backup is  Successfull")


sched = BackgroundScheduler()
# DO A TASK AFTER 1 MINUTE
sched.add_job(job_function, 'interval', minutes=1)
# DO A IN 2 AM (according to 24hour  format)
sched.add_job(database_backup, 'cron', hour=20, minute=7)
sched.start()
