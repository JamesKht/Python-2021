import os

now_path = os.getcwd()  #获取当前文件路径
print(os.getcwd())
print(type(os.getcwd()))


#写入文件方法一
with open(now_path+'\\123.txt','w',encoding='utf-8') as f:
      f.write("Success")
      f.close
      print("成功写入文件123.txt")

#写入文件方法二
f=open(now_path+'\\456.txt','w',encoding='utf-8')    #在目标路径创建相应文件
f.write('Success') #将下载到的图片数据写入文件
f.close()
print("成功写入文件456.txt")

#删除文件
if os.path.exists('123.txt'):    #判断文件是否存在
      os.remove('123.txt')
      print('成功删除文件')

#新建路径（新建文件夹）相对路径
if not os.path.exists('文件夹1'):    #判断文件是否存在
      os.makedirs('文件夹1')
      print("成功创建文件夹1")

#新建路径（新建文件夹）绝对路径
if not os.path.exists(now_path+'\\文件夹2'):    #判断文件是否存在
      os.makedirs('文件夹2')
      print("成功创建文件夹2")
            
                              

