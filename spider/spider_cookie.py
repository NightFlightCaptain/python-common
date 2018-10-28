# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'
from urllib import request, error
import json

if __name__ == '__main__':
    url = 'https://m.weibo.cn/api/container/getIndex' \
          '?containerid=5646903739_-_WEIBO_SECOND_PROFILE_WEIBO&page_type=03&page='

    proxy = {'http':'119.123.247.35:9000'}
    proxy_support = request.ProxyHandler(proxy)
    opener = request.build_opener(proxy_support)
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    # 安装Opener
    request.install_opener(opener)

    for i in range(1,20):
        url = url + str(i)

        response = request.urlopen(url)
        html = response.read().decode('utf-8')
        text = json.loads(html).get('data')
        print('**************************\n',i)
        for content in text.get('cards'):
            if content.get('card_type')!=9:
                break
            # print(content['mblog']['text'])
            print(content.get('mblog').get('text'))
        print('****************************\n')

