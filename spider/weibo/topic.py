# -*- coding:utf-8 -*-
# @Time      :2019/4/1 20:19
# @Author    :小栗旬
import csv
import json
import re

from bs4 import BeautifulSoup

from spider.spider_tools.Req import Req

csv_headers = ['用户名',
               '文本内容',
               '发布时间',
               '点赞数',
               '评论数',
               '转发数']

def get_all():
    write_csv_header(csv_headers)
    '''
        range中的参数第一个固定为2，第二个视情况而定，如果你要爬取的话题下很多微博，就设置大一点
    '''
    for i in range(2, 10):
        get_topic_all(i)


def get_topic_all(page):
    url = "https://m.weibo.cn/api/container/getIndex"
    """
    这个param复制你要爬取的话题的消息头内容，page不用复制。
    """
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
        mblog = content.get('mblog')
        id = mblog.get('id')

        title = mblog.get('text')
        time = mblog.get('created_at')
        comments_count = mblog.get('comments_count')
        reposts_count = mblog.get('reposts_count')
        attitudes_count = mblog.get('attitudes_count')
        soup = BeautifulSoup(title)
        user_name = mblog.get('user').get('screen_name')
        csv_c = {'用户名': user_name,
                 '文本内容': soup.get_text(),
                 '发布时间': time,
                 '点赞数':attitudes_count,
                 '评论数': comments_count,
                 '转发数': reposts_count}
        write_csv_rows(csv_headers,csv_c)


def write_csv_header(csv_headers):
    with open("cc.csv", 'w', encoding='utf-8-sig', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writeheader()


def write_csv_rows(csv_headers, rows):
    with open("cc.csv", 'a', encoding='UTF-8', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writerow(rows)

        # content_url = 'https://m.weibo.cn/comments/hotflow'
        # content_param = {
        #     'id': id,
        #     'mid': id,
        #     'max_id_type': 0
        # }

        # content_res = Req.post(content_url, content_param)
        # content_datas = json.loads(content_res.text).get('data')
        # if content_datas == None:
        #     continue
        # content_datas = content_datas.get('data')

        # with open(soup.get_text() + ".txt", "w", encoding="utf-8") as f:
        #     for content_data in content_datas:
        #         text = content_data.get('text')
        #         pattern = re.compile(r'<bound method Tag.get_text of <html><body><p>^</p></body></html>>')
        #         result = pattern.sub('', text)
        #         soup = BeautifulSoup(result)
        #         f.write(soup.get_text() + "\n")


if __name__ == '__main__':
    get_all()
