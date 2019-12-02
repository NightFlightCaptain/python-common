# -*- coding:utf-8 -*-
# @Time      :2019/2/23 14:04
# @Author    :小栗旬
import requests

from spider.spider_tools.Ip_List_Getter import Ip_List_Getter


class Req:
    """
    包装类，自动使用了ip代理，并包装了headers头
    """
    ip_getter = Ip_List_Getter()
    ip_getter.get_ip_list_from_txt()

    selfheaders = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X12; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
        # "Host": "www.shixiseng.com",
        "Pragma": "no-cache",
        # "Referer": "https://www.shixiseng.com/",
        "Upgrade-Insecure-Requests": "1"
    }

    # proxy = {
    #     "https": "61.128.208.94:3128"
    # }

    @classmethod
    def get(cls, url, params=None,headers=selfheaders):
        status_code = 0
        r = None
        ip = cls.ip_getter.get_a_useful_ip()
        while status_code != 200:
            try:
                proxy = {
                    ip[0]: ip[1]
                }
                r = requests.get(url=url, headers=headers, params=params, proxies=proxy)
                status_code = r.status_code
            except Exception as err:
                cls.ip_getter.ip_list.remove(ip)
                ip = cls.ip_getter.get_a_useful_ip()
        return r

    @classmethod
    def post(cls, url, params=None,headers=selfheaders):
        status_code = 0
        r = None
        ip = cls.ip_getter.get_a_useful_ip()
        while status_code != 200:
            try:
                proxy = {
                    ip[0]: ip[1]
                }
                r = requests.post(url=url, headers=headers, params=params, proxies=proxy)
                status_code = r.status_code
            except Exception:
                ip = cls.ip_getter.get_a_useful_ip()
                cls.ip_getter.ip_list.remove(ip)
        return r
