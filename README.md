# lagouSpider
lagouspider 是一个利用scrapy爬取拉勾网招聘职位的程序
# 安装
git clone https://github.com/yaozp2n/lagouSpider.git  
所需运行环境,请看 ./requirements.txt  
数据库使用Mongodb存储，运行需要安装Mongodb，安装传送门  
https://www.mongodb.org/downloads  
# 运行  
以下命令统一运行在zhaopin/目录下，与scrapy.cfg文件同级目录  
scrapy crawl lagou  
