import requests

res = requests.get('http://bj.xiaozhu.com/')
print(res.text)