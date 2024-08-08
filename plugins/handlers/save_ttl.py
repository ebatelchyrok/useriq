from pyrogram.client import Client
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.enums import MessageMediaType

@Client.on_message((filters.photo | filters.video) & filters.private & ~filters.me & ~filters.bot )
async def save_ttl(app: Client, message: Message):
    chat = await app.get_chat(message.chat.id)
    match message.media:
        case MessageMediaType.PHOTO:
            if not message.photo.ttl_seconds:
                return
            file = await message.download(in_memory=True)
            await app.send_photo ("me", file, caption=f"Получено из {chat.title}", has_spoiler=True)
        case MessageMediaType.VIDEO:
            if not message.video.ttl_seconds:
                return
            file = await message.download(in_memory=True)
            await app.send_video ("me", file, caption=f"Получено из {chat.title}", has_spoiler=True)
