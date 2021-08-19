import requests
from lxml import etree

#url
url = "https://s.weibo.com/top/summary?sudaref=www.baidu.com"

#定义请求头
headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55"}

#获取html字符串
response = requests.get(url, headers = headers)
content = response.content.decode('utf8')
#print(content)

#etree解析
html = etree.HTML(content)

#XPath提取数据
rank = html.xpath('//tbody/tr[position()>1]/td[1]/text()')

title = html.xpath('//tbody/tr[position()>1]/td/a/text()')

data = html.xpath('//tbody/tr[position()>1]/td/span/text()')

href = html.xpath('//tbody/tr[position()>1]/td/a/@href')

url_path = 'https://s.weibo.com'

num = 0
for i in rank:
      #检测广告标识
      if i == '•':
            pass
      else: 
            print("{0:>2} {1:>7} {2:{3}<15}".format(i,data[num],title[rank.index(i)],chr(12288)))
            num+=1

            #XPath尝试获取导语数据，如果没有导语会产生错误，直接换行输出
            try:
                  title_url = 'https://s.weibo.com' + href[rank.index(i)]
                  title_response = requests.get(title_url, headers = headers)
                  title_content = title_response.content.decode('utf8')
                  title_html = etree.HTML(title_content)
                  daoyu = title_html.xpath('//div[@class="card card-topic-lead s-pg16"]/p/text()')
                  if len(daoyu) != 0:
                        print("{1}{1}{0}\n".format(daoyu[0],chr(12288)))
            except:
                  print("\n")

input("加载完毕")
            
            
      























