import requests

url = 'http://docs.python-requests.org/en/master/'
r = requests.get(url)

print(r.status_code)
