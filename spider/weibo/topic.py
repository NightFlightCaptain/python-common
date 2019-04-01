# -*- coding:utf-8 -*-
# @Time      :2019/4/1 20:19
# @Author    :小栗旬
import json
import re

from bs4 import BeautifulSoup

from spider.spider_tools.Req import Req


def get_all():
    for i in range(2, 10):
        get_topic_all(i)


def get_topic_all(page):
    url = "https://m.weibo.cn/api/container/getIndex"
    param = {
        'containerid': '231522type=1&t=10&q=#四川木里县森林火灾#',
        'extparam': '# 四川木里县森林火灾#',
        'luicode': '10000011',
        'lfid': '102803',
        'sudaref': 'm.weibo.cn',
        'display': 0,
        'retcode': 6102,
        'page_type': 'searchall',
        'page': page
    }

    response = Req.post(url, params=param)
    data = response.text
    contents = json.loads(data).get('data').get('cards')[0].get('card_group')
    for content in contents:
        id = content.get('mblog').get('id')

        title = content.get('mblog').get('text')
        soup = BeautifulSoup(title)
        content_url = 'https://m.weibo.cn/comments/hotflow'
        content_param = {
            'id': id,
            'mid': id,
            'max_id_type': 0
        }

        content_res = Req.post(content_url, content_param)
        content_datas = json.loads(content_res.text).get('data')
        if content_datas == None:
            continue
        content_datas = content_datas.get('data')

        with open(soup.get_text() + ".txt", "w", encoding="utf-8") as f:
            for content_data in content_datas:
                text = content_data.get('text')
                pattern = re.compile(r'<bound method Tag.get_text of <html><body><p>^</p></body></html>>')
                result = pattern.sub('', text)
                soup = BeautifulSoup(result)
                f.write(soup.get_text() + "\n")


if __name__ == '__main__':
    get_all()
