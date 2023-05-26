import requests
import os
from dotenv import load_dotenv
load_dotenv()

telegram_token = os.getenv("telegram_token")
telegram_chat_id = os.getenv("telegram_chat_id")
message = "Здесь напишите свое сообщение"

#url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
#print(requests.get(url).json())




def post_message(message,TOKEN=telegram_token,chat_id=telegram_chat_id):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # Эта строка отсылает сообщение

#post_message(telegram_token,telegram_chat_id,message)
