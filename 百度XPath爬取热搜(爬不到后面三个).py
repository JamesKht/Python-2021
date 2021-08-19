import requests
from lxml import etree
import os

#url
url = "https://www.baidu.com"

#请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}

#发送请求获取响应
response = requests.get(url,headers = headers)
content = response.content.decode('UTF-8')
with open('百度XPath爬取热搜榜.txt','w',encoding='utf-8') as f:
      f.write(content)
      f.close
      print("百度XPath爬取热搜榜.txt 写入成功！")

#网页解析
html = etree.HTML(content)

#XPath
contents = html.xpath('//ul/li/a/span[2]/text()')
print(contents)

url_contents = html.xpath('//ul[@class="s-hotsearch-content"]/li/a/@href')
#print(url_contents)

baidu = []
for content,url_content in zip(contents,url_contents):
      eg = {}
      eg = {
            "content":content,
            "url":url_content
            }
      baidu.append(eg)
for i in baidu:
      print(i)
input("输出完成")

'''
1、XPath路径还是需要结合XPath插件和爬取下来的HTML网页进行综合分析确定
'''


