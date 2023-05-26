import requests
import os
from dotenv import load_dotenv
load_dotenv()

telegram_token = os.getenv("telegram_token")
telegram_chat_id = os.getenv("telegram_chat_id")
telegtam_to = os.getenv("telegtam_to")


def get_chat_id(TOKEN=telegram_token):
    #Получить ID пользователя 
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    dict_chat_id = requests.get(url).json()
    username_from = dict_chat_id['result'][0]['message']['from']['username']
    if username_from == telegtam_to:
        return dict_chat_id['result'][0]['message']['from']['id']
    else: 
        print('Мне пока лень делать здесь цикл и проверять это,нет границ совершенству!!!')

    
def post_message(message,TOKEN=telegram_token,chat_id=telegram_chat_id):
    #Отпрвить сообщение в telegram
    if not chat_id :
        print ('telegram_chat_id не заданно, получаю get_chat_id по нику')
        chat_id = get_chat_id(TOKEN)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json()) # Эта строка отсылает сообщение одновременно в telegtam и bash

