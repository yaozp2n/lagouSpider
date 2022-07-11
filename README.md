# lagouSpider
lagouspider 是一个利用scrapy爬取拉勾网招聘职位的程序
# 安装
git clone https://github.com/yaozp2n/lagouSpider.git  
所需运行环境,请看 ./requirements.txt  
数据库使用Mongodb存储，运行需要安装Mongodb，安装传送门  
https://www.mongodb.org/downloads  
如果仅仅作为测试不需要使用Mongodb，可以注释settings.py下对应行

![image](https://user-images.githubusercontent.com/24678542/178177505-3df70704-6bdf-4802-9ad7-93374516b80a.png)  
本程序使用了代理池，在middlerwares.py文件加下填入代理池地址  
![image](https://user-images.githubusercontent.com/24678542/178177813-eb0f4c2c-c9ca-460c-af97-dd75eeae50a4.png)  
代理池的搭建，安装传送门  
http://blog.csdn.net/c406495762/article/details/72793480  

# 运行  
以下命令统一运行在zhaopin/目录下，与scrapy.cfg文件同级目录  
scrapy crawl lagou  
