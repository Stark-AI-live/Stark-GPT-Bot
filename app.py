import os
import requests
from StarkChat import starkchat
from pyrogram import *
from pyrogram.types import *

chatbot = starkchat.StarkChat()

API_ID = "" 
API_HASH = ""
BOT_TOKEN = ""
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
            return
        except Exception as e:
            print(e)
            try:
                r = requests.get(f"https://asia.api.gpt.starkai.live/api?message={question}&key={API_KEY}&client_id={user_id}")
                reply = r.json()["message"]
                await msg.edit(reply)
                return
            except Exception as e:
                print(e)
                try:
                    r = requests.get(f"https://us-east.api.gpt.starkai.live/api?message={question}&key={API_KEY}&client_id={user_id}")
                    reply = r.json()["message"]
                    await msg.edit(reply)
                    return
                except Exception as e:
                    print(e)
                    reply = chatbot.chat(question)
                    await msg.edit(reply)
                    return
@bot.on_message(filters.command("reset"))
async def reset(client, message):
        user_id = message.from_user.id
        TEXTS = "Trying To Send Reset Request..."
        msg = await message.reply(TEXTS)
        try:
                data1=requests.get(f"https://api.gpt.starkai.live/reset?client_id={user_id}")
                await msg.edit("US West Server has been Reeset!")
                data2=requests.get(f"https://asia.api.gpt.starkai.live/reset?client_id={user_id}")
                await msg.edit("Asia Server has been Reset!")
                data3=requests.get(f"https://eu.api.gpt.starkai.live/reset?client_id={user_id}")
                await msg.edit("Europe Server has been Reset!")
                data4=requests.get(f"https://us-east.api.gpt.starkai.live/reset?client_id={user_id}")
                await msg.edit("US East Server has been Reset!")
                await msg.edit("Reset Requests has been Sent Successfully!")
        except Exception as e:
                await msg.edit("Unable to Reset User Data's")
        
        

def main():
     bot.run()



if __name__ == "__main__":
     main()
