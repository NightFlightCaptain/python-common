# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

import urllib.request
import json
from urllib import request


class WeiboSpider(object):
    def __init__(self,id):
        self.id = id
        self.proxy_addr = '119.123.247.35:9000'
        self.containerid = 0

    '''
    定义页面打开函数
    '''
    def use_proxy(self, url):
        req = request.Request(url)
        req.add_header('User-Agent',
                       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
        proxy = urllib.request.ProxyHandler({'http': self.proxy_addr})
        opener = urllib.request.build_opener(proxy,request.HTTPHandler)
        request.install_opener(opener)

        data = request.urlopen(req).read().decode('utf-8')
        return data

    # 获取containerid
    def get_containerid(self,content):
        for tab in content.get('tabsInfo').get('tabs'):
            if tab.get('tab_type')== 'weibo':
                self.containerid = tab.get('containerid')
                break

    # 获取用户信息
    def get_userinfo(self):
        url = 'https://m.weibo.cn/api/container/getIndex?uid='+str(self.id)+'&type=uid&value='+str(self.id)
        data = self.use_proxy(url)
        content = json.loads(data).get('data')

        # 获取containerid
        for tab in content.get('tabsInfo').get('tabs'):
            if tab.get('tab_type')== 'weibo':
                self.containerid = tab.get('containerid')

        # 获取用户信息
        user_info = content.get('userInfo')
        userInfo = {}
        userInfo['name'] = user_info['screen_name']
        userInfo['description'] = user_info['description']
        userInfo['follow_count'] = user_info['follow_count']
        userInfo['followers_count'] = user_info['followers_count']
        return userInfo

    '''
    获取微博内容
    '''
    def get_weibo(self):
        i =0
        while True:
            url = 'https://m.weibo.cn/api/container/getIndex?uid='+str(self.id)+'&type=uid&value='+str(self.id)+\
                  '&containerid='+str(self.containerid)+'&page='+str(i)
            try:
                data = self.use_proxy(url)
                content = json.loads(data).get('data')
                cards = content.get('cards')
                if len(cards) > 0:
                    for j in range(len(cards)):
                        # print("-------------正在爬取第"+str(i)+"页，第"+str(j)+"条微博")
                        if cards[j].get('card_type') == 9:
                            mblog = cards[j].get('mblog')
                            if mblog.__contains__('retweeted_status'):
                                isSelf = False
                            else:
                                isSelf = True
                            text = mblog.get('text')
                            print("原创" if isSelf else "转载"," 内容："+text)
                    i+=1
                else:
                    break
            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    w = WeiboSpider(id)
    w.get_userinfo()
    w.get_weibo()