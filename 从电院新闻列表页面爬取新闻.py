import requests
import os    #保存读取删除文件所用到的库
from bs4 import BeautifulSoup
import json
import re

def url_text(url):   #爬取并保存网页
      try:
            if not os.path.exists(root):
                  os.mkdir(root)
            if not os.path.exists(path):
                  r = requests.get(url)
                  r.encoding = r.apparent_encoding
                  #print(r.text)     输出获取到的网页
                  '''
                  with open(path, 'w',encoding='utf-8') as f:     #保存获取到的网页
                        f.write(r.text)
                        f.close()
                        print("Success!")
                  '''
                  return r.text
            else:
                  print("文件已存在")
      except:
            print("Error!")
            return "Error!"

def get_news_url(text):   #解析网页内容
      news_list = []
      soup = BeautifulSoup(text, 'html.parser')   #解析器解析网页
     #print(soup.prettify())
      i = 0
      for a in soup.h3.next_sibling:    #h3作为参考点比较好定位新闻位置，遍历h3下面的标签
            url = a.get('href')        #获取标签a上面的url
            #print(url)                 #输出，控制台观察
            a_div_list = a.find_all('div')#分割div分别获取标题和时间
            for b in a_div_list[0].children:#遍历第一个div这样可以获得标题
                  if b.name!='span':
                        url_name = b
                        #print(b)
            url_time = a_div_list[1].string
            #print(a_div_list[1].string)   #第二个div里面只有时间
            #print('\n')
            news_list.append([])
            news_list[i].append(url)
            news_list[i].append(url_name)
            news_list[i].append(a_div_list[1].string)
            i = i + 1
      return news_list

def list_2_dict(lists,url,name,data):    #news_dict转news_json
      dict_list = []
      for i in lists:
            new_dict = {url:i[0],name:i[1],data:i[2]}
            dict_list.append(new_dict)
      print(dict_list)
      return dict_list

def download_json(json,path):        #下载获取到的url,标题，发布时间的json格式
      try:
            os.remove(path)       #删除上一次调试过程中的文件
            print("删除成功")
      except:
            pass

      if not os.path.exists(path):
            with open(path, 'w',encoding='utf-8') as f:     #保存获取到的网页
                  f.write(json)
                  f.close()
                  print("Success!")
      else:
            print("文件已存在")
            

def download_news(news_dict):
      i = 0
      with open(news_dict[i]['data'][0:10] + news_dict[i]['name']+'.txt', 'w',encoding='utf-8') as f:
            f.write(news_dict[i]['name'])
            f.write(news_dict[i]['url'])
            f.close




def download_article(url, name, data, pos):    #爬取新闻正文网页内容，如果文章不可爬取则返回
      
      root= 'https://see.xidian.edu.cn'   #图片链接的一致格式

      r = requests.get(url, timeout=30)
      r.raise_for_status()
      r.encoding = r.apparent_encoding    #解析网页

      try:
           os.remove(name+'.txt')         #调试过程中的一步，可忽略
      except:
            pass

      '''
      with open(name+'.txt','w',encoding='utf-8') as f:    #调试过程中的一步，可忽略。这一步是为了查看网页代码
            f.write(r.text)
            f.close
      '''
      
      soup = BeautifulSoup(r.text,'html.parser')      #bs4解析
      #print(soup.prettify)     #输出soup

      article = soup.h1.next_sibling.next_sibling.next_sibling     #通过特征tag(h1)找到文字的位置
      #print(type(article))

      news_word = ''    #文章正文内容暂存
      news_img = []
      num=0
      for a in article:    #文本内容爬取
            num = num + 1
            try:
                  news_word = news_word + a.get_text()    #文字内容爬取
                  for i in a.children:
                        if i.name == 'img':
                              news_word = news_word + "\n图\n"    #图片位置标记
                              temp_url = root + i.get('src')     #图片网页记录
                              image = requests.get(temp_url)
                              f=open(pos + data[0:10] + name + str(num) +'.png','wb')    #在目标路径创建相应文件
                              f.write(image.content) #将下载到的图片数据写入文件
                              f.close()
                              
            except:
                  pass
      try:
            with open(pos+data[0:10]+name+".txt", 'w',encoding='utf-8') as f:     #保存获取到的新闻文字
                  f.write(news_word)
                  f.close()
                  
      except:
            return data[0:10]+name    #返回有问题的新闻





if __name__ == "__main__":
      url = "https://see.xidian.edu.cn/html/category/1.html"
      now_path = os.getcwd()
      root = now_path+"//学校新闻信息爬取内容保存//"
      path = root + "news.txt"
      try:
            os.remove(path)       #删除上一次调试过程中的文件
      except:
            pass
      news_soup = url_text(url)
      #print(news_soup)        #输出网页上获取到的内容
      news_list = get_news_url(news_soup)    #二维列表
      #print(news_list)        #输出获取到的url,标题，发布时间
      news_dict = list_2_dict(news_list,"url","name","data")     #元素是字典的列表
      news_json = json.dumps(news_dict,indent = 3,ensure_ascii= False)   #是字符串类型
      #print(news_json)        #输出获取到的url,标题，发布时间的json格式
      #download_json(news_json,root + "news.json")
      #download_news(news_dict)
      error_article = []
      for i in news_dict:  #把获取到的新闻网址一个个访问
            error_article.append(download_article(i['url'],i['name'],i['data'],root))
            print(i)    #输出对应的字典，显示进程
      new_lst_1 = [i for i in error_article if i is not None]   #删除None的值
      print(new_lst_1)

      
      
      






