import os
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument
import pandas as pd
import config
from PIL import Image
import requests

# Ensure directories exist
os.makedirs("data/raw", exist_ok=True)
os.makedirs("data/images", exist_ok=True)

# ✅ Fix: pass `client` to the function
async def download_media(client, message, channel_name):
    if message.media:
        try:
            file_path = f"data/images/{channel_name}_{message.id}"
            if isinstance(message.media, MessageMediaPhoto):
                await client.download_media(message, file_path + ".jpg")
                return file_path + ".jpg"
            elif isinstance(message.media, MessageMediaDocument):
                await client.download_media(message, file_path + ".pdf")
                return file_path + ".pdf"
        except Exception as e:
            print(f"Media download failed: {e}")
    return None

async def scrape_channel(client, channel_name):
    channel = await client.get_entity(channel_name)
    messages = await client.get_messages(channel, limit=300)

    data = []
    for msg in messages:
        # ✅ Fix: pass `client` to `download_media()`
        media_path = await download_media(client, msg, channel_name)
        data.append({
            "date": msg.date,
            "message": msg.text,
            "channel": channel_name,
            "media_path": media_path,
            "has_media": bool(msg.media)
        })

    return pd.DataFrame(data)

async def main():
    async with TelegramClient(config.SESSION_NAME, config.API_ID, config.API_HASH) as client:
        all_data = []
        for channel in config.CHANNELS:
            print(f"Scraping {channel}...")
            df = await scrape_channel(client, channel)
            all_data.append(df)

        final_df = pd.concat(all_data)
        final_df.to_csv("data/raw/telegram_messages.csv", index=False)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
