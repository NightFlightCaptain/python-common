# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

import json

import time

from spider.spider_tools.Req import Req


class FileWriter(object):
    def writer(self, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.write(text + '\n')


class WeiboSpider(object):
    def __init__(self, id):
        self.file_writer = FileWriter()
        self.id = id
        self.containerid = 0

    # 获取containerid
    def get_containerid(self, content):
        for tab in content.get('tabsInfo').get('tabs'):
            if tab.get('tab_type') == 'weibo':
                self.containerid = tab.get('containerid')
                break

    # 获取用户信息
    def get_userinfo(self):
        url = 'https://m.weibo.cn/api/container/getIndex?uid=' + str(self.id) + '&type=uid&value=' + str(self.id)
        data = Req.get(url).content
        content = json.loads(data).get('data')

        # 获取containerid
        for tab in content.get('tabsInfo').get('tabs'):
            if tab.get('tab_type') == 'weibo':
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
        i = 0
        while True:
            url = 'https://m.weibo.cn/api/container/getIndex?uid=' + str(self.id) + '&type=uid&value=' + str(self.id) + \
                  '&containerid=' + str(self.containerid) + '&page=' + str(i)
            try:
                data = Req.get(url).content
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
                            status = "原创" if isSelf else "转载"
                            data = status + " 内容：" + text
                            # print(data)
                            self.file_writer.writer(str(self.id)+"_"+str(time.strftime('%Y%m%d', time.localtime(time.time())))+"_weibo_contain.txt", data)

                    i += 1
                else:
                    break
            except Exception as e:
                print(e)
                pass


if __name__ == "__main__":
    w = WeiboSpider()
    w.get_userinfo()
    w.get_weibo()
