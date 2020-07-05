import requests

url = "https://item.jd.com/100008348542.html"

hd = {'user-agent': 'Chrome/83'}

try:
    r = requests.get(url, headers=hd)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except Exception as e:
    raise e


url = "https://www.amazon.cn/gp/product/B01M8L5Z3Y"

try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except Exception as e:
    raise e


keyword = 'Python'

try:
    kv = {'wd': keyword}
    r = requests.get("http://www.baidu.com/s", headers=hd, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except Exception as e:
    raise e


try:
    kv = {'ie': 'utf-8', 'fr': 'none', 'src': 'home_none', 'q': keyword}
    r = requests.get("http://www.so.com/s", params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except Exception as e:
    raise e



import os

path = "./"

url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"

path = path + url.split('/')[-1]

try:
    r = requests.get(url)
    r.raise_for_status()
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("Image saved successfully.")
    else:
        print('File exists already.')
except Exception as e:
    raise e


ip = '202.204.80.112'
url = 'http://m.ip138.com/ip.asp?ip=' + ip
print(url)
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except Exception as e:
    raise e