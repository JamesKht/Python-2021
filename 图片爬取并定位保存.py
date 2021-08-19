import requests
import os

url = "https://tse1-mm.cn.bing.net/th/id/R-C.5e38a5b5277c277cd6cdaa7be7384dfd?rik=VXmrgfjBW8ovjQ&riu=http%3a%2f%2fpic15.nipic.com%2f20110703%2f7727434_193100046150_2.jpg&ehk=GB6%2futnVVcspuFLnfgw03PdUm%2ftXOMuq92NfI1SzpIU%3d&risl=&pid=ImgRaw"
root = "C://Users//康昊天//Desktop//微博爬虫//学习//"
path = root + "maomi.jpg"
try:
      if not os.path.exists(root):
            os.mkdir(root)
      if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                  print(1)
                  f.write(r.content)
                  f.close()
                  print("Success!")
      else:
            print("文件已存在")
except:
      print("Failed!")
