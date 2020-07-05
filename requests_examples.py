import requests

r = requests.head('http://httpbin.org/get')

r.headers

r.text

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('http://httpbin.org/post', data = payload)

print(r.text)
print('------------------------------------------------------------')

r = requests.post('http://httpbin.org/post', data = 'ABC')

print(r.text)
print('------------------------------------------------------------')

r = requests.put('http://httpbin.org/put', data = payload)

print(r.text)
print('------------------------------------------------------------')

kv = payload

r = requests.request('GET', 'http://python123.io/ws', params=kv)

print(r.url)
print('------------------------------------------------------------')

r = requests.request('POST', 'http://httpbin.org/post', data=kv)

print(r.text)
print('------------------------------------------------------------')

r = requests.request('POST', 'http://httpbin.org/post', data='main text')

print(r.text)
print('------------------------------------------------------------')

r = requests.request('POST', 'http://httpbin.org/post', json=kv)

print(r.text)
print('------------------------------------------------------------')

r = requests.request('POST', 'http://httpbin.org/post', json='json')

print(r.text)
print('------------------------------------------------------------')

hd = {'user-agent': 'Chrome/10'}

r = requests.request('POST', 'http://httpbin.org/post', headers=hd)

print(r.text)
print('------------------------------------------------------------')

fs = {'file': open('getHTMLText.py', 'r')}

r = requests.request('POST', 'http://httpbin.org/post', files=fs)

print(r.text)
print('------------------------------------------------------------')

r = requests.request('GET', 'http://www.baidu.com', timeout=10)

pxs = { 'http': 'http://user:pass@10.10.10.1:1234', 'https': 'https://10.10.10.1:4321'}

r = requests.request('GET', 'http://www.baidu.com', proxies=pxs, timeout=10)