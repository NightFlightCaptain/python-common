# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'
import sys

import requests
from bs4 import BeautifulSoup


class XiaoshuoDownloader(object):

    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.server_target = 'https://www.biqukan.com/57_57456/'
        self.names = []
        self.urls = []
        self.num = 0

    def get_downloader_url(self):
        req = requests.get(url=self.server_target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_='listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.num = len(a[12:])  # delete duplicate chapters

        for each in a[12:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_='showtxt')
        texts = texts[0].text.replace('\xa0' * 8, '\n\n')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = XiaoshuoDownloader()
    dl.get_downloader_url()
    print("开始下载")
    for i in range(dl.num):
        dl.writer(dl.names[i], "变身之我真不是NPC.txt", dl.get_contents(dl.urls[i]))
        sys.stdout.write(" 已经下载:%.3f%%" % float(i / dl.num) + "\r")
        sys.stdout.flush()
    print("下载完成")
