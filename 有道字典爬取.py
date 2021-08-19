import requests
import win32api
from bs4 import BeautifulSoup

def input_word():       #输入英文单词，返回网页链接
      word = input("请输入英文单词:")
      root = "http://www.youdao.com/w/"
      url = root+word
      return url

def get_html(url):
      try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
      except:
            return 'Error'

def print_trans(text):
      trans = {}
      soup = BeautifulSoup(text, 'html.parser')
      pronounce = soup.h2
      prolist = []
      for link in pronounce.find_all('span'):
            prolist.append(link)
      for i in prolist:
            if i.get('class')[0] == 'pronounce':
                  print(i.text[0],end = ':')
            elif i.get('class')[0] == 'phonetic':
                  print(i.text)
            else:
                  print(i.text)
      print("\n释义：\n", end = '')
      trans = soup.h2.next_sibling.next_sibling
      for i in trans.find_all('li'):
            print(i.text)
      print("\n")
      for i in trans.find_all('p'):
            print(i.string.replace("\n","").replace("  ",""))
      return ""

def add_to_list():
      return""


if __name__ == "__main__":
      while True:
            try:
                  url = input_word()
                  text = get_html(url)
                  print_trans(text)
                  print('-----------------------------------------------------------------------')
            except:
                  print('-------------------------输入有误，请重新输入！-------------------------')

      
