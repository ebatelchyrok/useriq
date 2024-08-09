from app import app, tz
from datetime import datetime, timedelta
from asyncio import sleep


async def infect():
    schudled_time = datetime.now(tz=tz)
    for _ in range(72):
        schudled_time += timedelta(minutes=20)
        await app.send_message(chat_id=int (-1002175276391), text="Заразить +", schedule_date=schudled_time)
        await sleep(7)
        
