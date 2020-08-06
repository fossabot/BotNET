import requests

def postDDoS(url, data):
    r = requests.post(url, data=data)
    print(r.status_code)
