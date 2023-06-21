import os
import requests
from StarkChat import starkchat
from pyrogram import *
from pyrogram.types import *

chatbot = starkchat.StarkChat()

API_ID = "" 
API_HASH = ""
BOT_TOKEN = ""
CHAT_ID = ""
API_KEY = ""

bot = Client("STARK", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@bot.on_message(filters.text)
async def response(client, message):
        question = message.text
        user_id = message.from_user.id
        TEXTS = "Thinking..."
        msg = await message.reply(TEXTS)
        try:
            r = requests.get(f"https://api.gpt.starkai.live/api?message={question}&key={API_KEY}&client_id={user_id}")
            reply = r.json()["message"]
            await msg.edit(reply)
            TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`\n**Engine:** `API`"
            await bot.send_message(chat_id=CHAT_ID,text=TEXT)
            return
        except Exception as e:
            print(e)
            try:
                r = requests.get(f"https://asia.api.gpt.starkai.live/api?message={question}&key={API_KEY}&client_id={user_id}")
                reply = r.json()["message"]
                await msg.edit(reply)
                TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`\n**Engine:** `API`"
                await bot.send_message(chat_id=CHAT_ID,text=TEXT)
                return
            except Exception as e:
                print(e)
                try:
                    r = requests.get(f"https://us-east.api.gpt.starkai.live/api?message={question}&key={API_KEY}&client_id={user_id}")
                    reply = r.json()["message"]
                    await msg.edit(reply)
                    TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`\n**Engine:** `API`"
                    await bot.send_message(chat_id=CHAT_ID,text=TEXT)
                    return
                except Exception as e:
                    print(e)
                    reply = chatbot.chat(question)
                    await msg.edit(reply)
                    TEXT = f"**Question:** `{question}`\n**Response:** `{reply}`\n**Engine:** `Library`"
                    await bot.send_message(chat_id=CHAT_ID,text=TEXT)
                    return


def main():
     bot.run()
     bot.send_message(chat_id=CHAT_ID,text="Started...")


if __name__ == "__main__":
     main()
