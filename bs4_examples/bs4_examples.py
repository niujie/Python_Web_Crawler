import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text

soup = BeautifulSoup(demo, "html.parser")
# print(soup.prettify())
# print(soup.a.prettify())

# soup = BeautifulSoup("<p>text</p>", "html.parser")

# print(soup.title)

# tag = soup.a
# print(tag.name)
# 
# print(tag.parent.name)
# print(tag.parent.parent.name)
# print(tag.attrs)
# print(tag.attrs['class'])
# print(tag.attrs['href'])
# print(type(tag.attrs))
# print(type(tag))
# print(tag.string)
# 
# print(soup.p)
# print(type(soup.p.string))

# newsoup = BeautifulSoup("<b><!--This is a comment--></b><p>This is not a comment</p>", "html.parser")
# print(newsoup.b.string)
# print(type(newsoup.b.string))
# print(newsoup.p.string)
# print(type(newsoup.p.string))

# print(soup.head)
# print(soup.head.contents)

# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])

# print(soup.title.parent)

# print(soup.html.parent)

# print(soup.parent)

# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)

# print(soup.a.parent)

# for sibling in soup.a.next_siblings:
#     print(sibling)

# for sibling in soup.a.previous_siblings:
#     print(sibling)

# soup = BeautifulSoup("<p>中文</p>", "html.parser")

# print(soup.p.string)

# print(soup.p.prettify())

# for link in soup.find_all('a'):
    # print(link.get('href'))

# print(soup.find_all(['a', 'b']))

# for tag in soup.find_all(True):
#     print(tag.name)

# import re
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)

# print(soup.find_all('p', 'course'))

# print(soup.find_all(id='link1'))

# import re
# print(soup.find_all(id=re.compile('link')))

# print(soup.find_all('a', recursive=False))

# import re
# print(soup.find_all(string = re.compile("python")))