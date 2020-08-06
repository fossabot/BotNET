import requests

def getDDoS(url):
    r = requests.get(url)
    print(r.status_code)

