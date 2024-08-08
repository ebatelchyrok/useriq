import logging
import os

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv
from pyrogram.client import Client
from pytz import timezone
import patch_peer

logging.basicConfig(level=logging.CRITICAL)
logger = logging.getLogger(__name__)

load_dotenv()

session = str (os.getenv("SESSION"))
plugins = dict(root="plugins")

tz = timezone("Europe/Kiev")
jobstores = {
    "default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")
}

app = Client("my_account", in_memory=True, session_string=session, plugins=plugins)
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=tz)
