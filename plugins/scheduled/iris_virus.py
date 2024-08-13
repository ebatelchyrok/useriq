from app import app, tz
from datetime import datetime, timedelta
from asyncio import sleep

async def infect():
    for i in range(1, 73):
        schudled_time = datetime.now(tz=tz) + timedelta(minutes=20 * i)
        await app.send_message(chat_id=int(-1002175276391), text="Заразить +", schedule_date=schudled_time)
        await sleep(5)
