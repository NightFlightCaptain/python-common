# -*- coding:utf-8 -*-
# @Time      :2019/1/2 16:15
# @Author    :小栗旬
import random
import re

from lxml import etree
from urllib import request
import json
import requests
from bs4 import BeautifulSoup
import jieba

from spider.Ip_List_Getter import Ip_List_Getter


def get_hotels_list():
    user_agent_list = [
        # 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        # 'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        # 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        # 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        # 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        # 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        # 'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        # 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        # 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        # 'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    ]

    ip_getter = Ip_List_Getter()
    ip_getter.get_ip_list_from_txt()

    hotel_list = []

    def get_hotels_action():
        """

        :return:返回一个元祖，（hotel_id,hotel_title,hotel_href)
        """
        index_url = "http://hotels.ctrip.com/Domestic/Tool/AjaxIndexHotSaleHotelNew.aspx?traceid=1754008866826253798"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": random.choice(user_agent_list)
        }
        params = {
            "city": 477,
            "cityName": "武汉",
            "cityPY": "WuHan",
            "psid": ""
        }

        ip = ip_getter.get_a_useful_ip()
        proxy = {
            ip[0]: ip[1]
        }
        r = requests.post(index_url, params=params, headers=headers, proxies=proxy)
        html = r.text
        print("************************************************")
        print("************************************************")
        print("************************************************")
        print("************************************************")
        div_all = BeautifulSoup(html, "html.parser")
        div_find = div_all.find_all('a', attrs={'class': 'hotel_abbrpic'})

        for div in div_find:
            title = re.search(r'title="(.*?)"', str(div))
            id = re.search(r'data-hotel="(.*?)"', str(div))
            hotel_list.append((id.group(1).split('|')[0], title.group(1)))
            print(hotel_list[-1])

    def get_hotels_action2():
        """

        :return:返回一个元祖，（hotel_id,hotel_title)
        """
        index_url = "http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "hotels.ctrip.com",
            "User-Agent": random.choice(user_agent_list)
        }

        for page in range(1,10):
            params = {
                "StartTime": "2019-01-03",
                "DepTime": "2019-01-04",
                "cityId": 477,
                "cityPY": "wuhan",
                "cityCode": "027",
                "page":page
            }

            ip = ip_getter.get_a_useful_ip()
            proxy = {
                ip[0]: ip[1]
            }
            print("************************************************")
            print("************************************************")
            print("************************************************")
            print("************************************************")
            r = requests.post(index_url, params=params, headers=headers, proxies=proxy)
            html = r.text
            r.encoding = "utf-8"

            j = json.loads(html)
            hotel_full_list = j.get("hotelPositionJSON")
            for hotel_full in hotel_full_list:
                hotel_list.append((hotel_full.get("id"),hotel_full.get("name")))
                print(hotel_list[-1])
        return hotel_list

    def get_hotel_detail(id):
        """
        直接进入页面的时候获取到的comment是以html的形式发送的

        :param id: 酒店id
        :return:
        """
        index_url = "http://m.ctrip.com/webapp/hotel/hoteldetail/dianping/" + id + ".html"

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Host": "m.ctrip.com",
            "User-Agent": random.choice(user_agent_list)
        }
        params = {
            "fr": "detail",
            "atime": "20190102",
            "days": 1
        }
        ip = ip_getter.get_a_useful_ip()
        proxy = {
            ip[0]: ip[1]
        }

        r = requests.get(url=index_url, params=params, headers=headers, proxies=proxy)
        r.encoding = "utf-8"
        html = r.text
        contents = re.findall(r'<p class="tree-ellips-line6">(.*?)</p>', html)
        for c in contents:
            print(c)

    def get_hotel_detail2( id):
        url = "http://m.ctrip.com/restapi/soa2/14605/gethotelcomment?_fxpcqlniredt=09031164210005207654"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Host": "m.ctrip.com",
            "User-Agent": random.choice(user_agent_list)
        }

        params = {"hotelId": id,
                  "pageIndex": 2,
                  "tagId": 0,
                  "pageSize": 30,
                  "groupTypeBitMap": 2,
                  "needStatisticInfo": 0,
                  "order": 0,
                  "basicRoomName": "",
                  "travelType": -1,
                  "head": {"cid": "09031164210005207654",
                           "ctok": "",
                           "cver": "1.0",
                           "lang": "01",
                           "sid": "8888",
                           "syscode": "09",
                           "auth": "",
                           "extension": []
                           }
                  }
        ip = ip_getter.get_a_useful_ip()
        print(ip)
        proxy = {
            ip[0]: ip[1]
        }

        r = requests.post(url=url, data=json.dumps(params), headers=headers, proxies=proxy)
        r.encoding = "utf-8"
        html = r.text
        j = json.loads(html)
        comment_list = j.get("othersCommentList")
        return comment_list
        # for comment in comment_list:
        #     print(comment.get("content"))

    get_hotels_action2()

    for hotel in hotel_list:
        comment_list = get_hotel_detail2(id=hotel[0])
        with open("hotel_comment/" + hotel[1] + ".txt", "w", encoding="utf-8") as f:
            for comment in comment_list:
                f.write(comment.get("content") + "\n")
        print("*******" + hotel[1] + "******")


if __name__ == "__main__":
    get_hotels_list()
