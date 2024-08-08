from app import app, tz
from datetime import datetime, timedelta
from asyncio import sleep


async def infect():
    current_time = datetime.now(tz=tz)
    for i in range(1, 73):
        schedule_time = current_time + timedelta(minutes=20 * i)
        await app.send_message(chat_id=int (-1002175276391), text="Заразить +", schedule_date=schedule_time)
        await sleep(7)
        
