from plugins.scheduled import infect
from app import scheduler

def jobs ():
    scheduler.add_job(infect, 'cron', hour=0, minute=0)
