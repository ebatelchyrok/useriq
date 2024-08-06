from pytz import timezone
import os
from dotenv import load_dotenv
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from pyrogram import Client

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

load_dotenv()

session = os.getenv("SESSION")
plugins = dict(root="plugins")

tz = timezone("Europe/Kiev")
jobstores = {
    "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}

app = Client("my_account", in_memory=True, session_string=session, plugins=plugins)
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=tz)
