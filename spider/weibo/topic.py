# -*- coding:utf-8 -*-
# @Time      :2019/4/1 20:19
# @Author    :小栗旬
import csv
import json
import os
import time

from bs4 import BeautifulSoup
from datetime import datetime, timedelta

from spider.spider_tools.Req import Req

csv_headers = ['用户名',
               '文本内容',
               '发布时间',
               '点赞数',
               '评论数',
               '转发数']


def get_hot_topic_top10():
    url = "https://m.weibo.cn/api/container/getIndex"
    param = {
        'containerid': '106003type=25&t=3&disable_hot=1&filter_type=realtimehot',
        'title': '微博热搜',
        'extparam': 'filter_type=realtimehot&mi_cid=100103&pos=0_0&c_type=30&display_time=1554296319',
        'luicode': 10000011,
        'lfid': 231583
    }
    res = Req.get(url, param)
    data = json.loads(res.text)
    hot_topics = data.get('data').get('cards')[0].get('card_group')

    cur_path = os.getcwd()
    dir_name = str(time.strftime('%Y%m%d', time.localtime(time.time())))
    dir_path = cur_path + os.path.sep + dir_name
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    for i in range(1, 11):
        hot_topic = hot_topics[i]
        topic_url = hot_topic.get('scheme')
        topic_desc = hot_topic.get('desc')
        print("搜索第"+str(i)+"个话题:"+topic_desc)
        get_one_topic_for_page(topic_url, topic_desc, dir_path)


def get_one_topic_for_page(url, desc, dir_path):

    url = "https://m.weibo.cn/api/container/getIndex?" + url.split('?')[1]
    write_csv_header(csv_headers, desc, dir_path)
    page_size = 10
    get_one_topic_first_page(url, desc, dir_path)
    for i in range(2, page_size + 1):
        print("搜索话题[" + desc + "]的第" + str(i) + "页")
        url_all = url + '&page=' + str(i)
        get_one_topic_from2(url_all, desc, dir_path)


def get_one_topic_first_page(url, desc, dir_path):
    print("搜索话题[" + desc + "]的第1页")
    response = Req.post(url)
    data = response.text
    contents = json.loads(data).get('data').get('cards')
    print(url)
    for content in contents:
        card_group = content.get('card_group')
        if card_group is None:
            continue
        mblog = card_group[0].get('mblog')
        if mblog is None:
            continue
        # id = mblog.get('id')
        title = mblog.get('text')
        time = time_handler(mblog.get('created_at'))
        comments_count = mblog.get('comments_count')
        reposts_count = mblog.get('reposts_count')
        attitudes_count = mblog.get('attitudes_count')
        soup = BeautifulSoup(title)
        user_name = mblog.get('user').get('screen_name')
        print(user_name+" "+time+" "+soup.get_text())
        csv_c = {'用户名': user_name,
                 '文本内容': soup.get_text(),
                 '发布时间': time,
                 '点赞数': attitudes_count,
                 '评论数': comments_count,
                 '转发数': reposts_count}
        write_csv_rows(csv_headers, csv_c, desc, dir_path)


def get_one_topic_from2(url, desc, dir_path):
    response = Req.post(url)
    data = response.text
    print(url)
    if json.loads(data).get('ok') == 0:
        return
    contents = json.loads(data).get('data').get('cards')
    for content in contents:
        mblog = content.get('mblog')

        # id = mblog.get('id')
        title = mblog.get('text')
        time = time_handler(mblog.get('created_at'))
        comments_count = mblog.get('comments_count')
        reposts_count = mblog.get('reposts_count')
        attitudes_count = mblog.get('attitudes_count')
        soup = BeautifulSoup(title)
        user_name = mblog.get('user').get('screen_name')
        print(user_name+" "+time+" "+soup.get_text())
        csv_c = {'用户名': user_name,
                 '文本内容': soup.get_text(),
                 '发布时间': time,
                 '点赞数': attitudes_count,
                 '评论数': comments_count,
                 '转发数': reposts_count}
        write_csv_rows(csv_headers, csv_c, desc, dir_path)


def write_csv_header(csv_headers, desc, dir_path):
    with open(dir_path + os.sep + desc + ".csv", 'w', encoding='utf-8-sig', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writeheader()


def write_csv_rows(csv_headers, rows, desc, dir_path):
    with open(dir_path + os.sep + desc + ".csv", 'a', encoding='UTF-8', newline='') as f:
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


def time_handler(publish_time):
    """
    微博时间格式处理
    :param publish_time:输入的微博时间
    :return: %Y-%m-%d %H:%M 格式
    """

    print(publish_time)
    if "刚刚" in publish_time:
        publish_time = datetime.now().strftime('%Y-%m-%d %H:%M')

    elif "分钟" in publish_time:
        minute = publish_time[:publish_time.find("分钟")]
        minute = timedelta(minutes=int(minute))
        publish_time = (datetime.now() - minute).strftime("%Y-%m-%d %H:%M")
    elif "小时" in publish_time:
        hour = publish_time[:publish_time.find("小时")]
        hour = timedelta(hours=int(hour))
        publish_time = (datetime.now() - hour).strftime("%Y-%m-%d %H:%M")
    elif "今天" in publish_time:
        today = datetime.now().strftime("%Y-%m-%d")
        time = publish_time.replace('今天', '')
        publish_time = today + " " + time
    elif "昨天" in publish_time:
        day = timedelta(days=1)
        today = (datetime.today()-day).strftime("%Y-%m-%d")
        publish_time = publish_time.replace('昨天',today)
    elif "月" in publish_time:
        year = datetime.now().strftime("%Y")
        publish_time = str(publish_time)
        publish_time = year + "-" + publish_time.replace('月', '-').replace('日', '')
    else:
        publish_time = publish_time[:16]
    print(publish_time)
    return publish_time


if __name__ == '__main__':
    print("爬取正在开始")
    get_hot_topic_top10()
    # url='https://m.weibo.cn/search?containerid=100103type%3D1%26t%3D10%26q%3D%23%E6%9E%97%E4%BF%8A%E6%9D%B0%E7%BB%99%E4%B8%8A%E5%8D%8A%E8%BA%AB%E6%89%93%E9%A9%AC%E8%B5%9B%E5%85%8B%23&isnewpage=1&extparam=filter_type%3Drealtimehot%26pos%3D0%26c_type%3D31%26realpos%3D0%26flag%3D16%26display_time%3D1554296611&luicode=10000011&lfid=106003type%3D25%26t%3D3%26disable_hot%3D1%26filter_type%3Drealtimehot'
    # url = "https://m.weibo.cn/api/container/getIndex?"+url.split('?')[1]
    # res = Req.get(url)
    #
    # print(res.text)
