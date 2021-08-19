import os
import requests
from bs4 import BeautifulSoup
import re

url = 'https://see.xidian.edu.cn/html/news/10972.html'
name = '学院组织参加西电第四届STEAM科技夏令营'
root= 'https://see.xidian.edu.cn'

r = requests.get(url, timeout=30)
r.raise_for_status()
r.encoding = r.apparent_encoding

try:
     os.remove(name+'.txt')
except:
      pass

with open(name+'.txt','w',encoding='utf-8') as f:
      f.write(r.text)
      f.close

soup = BeautifulSoup(r.text,'html.parser')
#print(soup.prettify)     #输出soup

article = soup.h1.next_sibling.next_sibling.next_sibling
#print(type(article))

for a in article:
      try:
            print(a.get_text())
            for i in a.children:
                  if i.name == 'img':
                        print(root + i.get('src'))
      except:
            pass

