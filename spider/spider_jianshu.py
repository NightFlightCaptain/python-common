# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

from urllib import request
from bs4 import BeautifulSoup

'''
    爬取简书首页的文章 标题和连接
'''
if __name__ =="__main__":
    url = "https://www.jianshu.com"
    headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                           ' Chrome/55.0.2883.87 Safari/537.36'}
    page = request.Request(url, headers=headers)
    page_info = request.urlopen(page).read().decode('utf-8')#打开Url,获取HttpResponse返回对象并读取其ResposneBody

    soup = BeautifulSoup(page_info,'html.parser')
    titles = soup.find_all('a','title')

    with open(r'D:\Github\untitled\spider\articles.txt','w') as file:
        for title in titles:
            file.write(title.string+'\n')
            file.write("https://www.jianshu.com"+title.get('href')+'\n\n')
