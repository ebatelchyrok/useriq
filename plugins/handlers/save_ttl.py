from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import MessageMediaType

@Client.on_message((filters.photo | filters.video | filters.document) & filters.private & ~filters.me)
async def save_ttl(app: Client, message: Message):
    match message.media:
        case MessageMediaType.PHOTO:
            if not message.photo.ttl_seconds:
                return
            file = await message.download(in_memory=True)
            await app.send_photo ("me", file, has_spoiler=True)
        case MessageMediaType.VIDEO:
            if not message.video.ttl_seconds:
                pass
            file = await message.download(in_memory=True)
            await app.send_video ("me", file, has_spoiler=True)
        case MessageMediaType.DOCUMENT:
            if not message.document.ttl_seconds:
                return
            file = await message.download(in_memory=True)
            await app.send_document ("me", file)
    
