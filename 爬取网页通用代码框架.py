import requests

def getHTMLText(url):
      try:
            r = requests.get(url, timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
      except:
            return 'Error'

if __name__ == "__main__":
      url = "https://see.xidian.edu.cn"
      print(getHTMLText(url))


'''
返回503
使用r.request.headers查看我们给网页的头部信息
通过建立字典  kv = {'user_agent':'Mozilla/5.0}
并修改参数    r = requests.get(url,headers=kv)
此时 可返回200
'''
      
