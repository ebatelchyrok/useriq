from pyrogram import Client, filters
from pyrogram.types import Message
import re

block_pattern = re.compile(r'🦠 Лорд Мефедрон ss.*?вы будете получать по (\d+) единиц[а-я]* био-ресурса', re.DOTALL)
resource_pattern = re.compile(r'вы будете получать по (\d+) единиц[а-я]* био-ресурса')
id_pattern = re.compile(r'подверг заражению патогеном «ИГИЛ» (\w+)')

#@Client.on_message (filters.regex(block_pattern) & filters.user("@iris_cm_bot"))
async def infect_handler (app: Client, message: Message):
    text = message.text
    if resource_pattern.search(text):
        return
    resource = int (resource_pattern.search(text).group(1))
    if resource < 50:
        return
    if id_pattern.search(text):
        return
    id = int (id_pattern.search(text).group(1))
    user = {id: resource}
        

