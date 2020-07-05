from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

print(soup)
print('------------------------------------------------------------')
print(soup.prettify())
print('------------------------------------------------------------')

match = soup.title
print(match)
print('------------------------------------------------------------')

match = soup.title.text
print(match)
print('------------------------------------------------------------')

match = soup.div
print(match)
print('------------------------------------------------------------')

match = soup.find('div')
print(match)
print('------------------------------------------------------------')

match = soup.find('div', class_='footer')
print(match)
print('------------------------------------------------------------')

article = soup.find('div', class_='article')
print(article)
print('------------------------------------------------------------')

headline = article.h2.a.text
print(headline)
print('------------------------------------------------------------')

summary = article.p.text
print(summary)
print('------------------------------------------------------------')

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)
    
    summary = article.p.text
    print(summary)

    print()
