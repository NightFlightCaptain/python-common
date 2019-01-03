# -*- coding:utf-8 -*-
# @Time      :2019/1/2 16:29
# @Author    :小栗旬

import random
from urllib import request
import json
import requests
from bs4 import BeautifulSoup


class Ip_List_Getter:
    """
    写一个爬取ip地址的类，以后可以直接调用
    """

    def __init__(self):
        self.ip_list = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }
        self.proxy = {
            "https": "119.101.112.116:9999"
        }

    def get_ip_list(self):
        """
        从网站爬取ip_list

        :return:ip_list，数组，元素类型是元祖，元祖第一个元素表示https或http，第二个元素表示ip地址
        """
        for page in range(1, 20):
            url = "http://www.xicidaili.com/nn/" + str(page)
            web_data = requests.get(url=url, headers=self.headers, proxies=self.proxy)
            print(web_data)
            soup = BeautifulSoup(web_data.text, "lxml")
            ips = soup.find_all('tr')
            print(ips)
            for i in range(2, len(ips)):
                ip_info = ips[i]
                print(ip_info)
                tds = ip_info.find_all('td')
                self.ip_list.append((tds[5].text, tds[1].text + ":" + tds[2].text))
            self.write_ip_list2txt()
        return self.ip_list

    def __write_ip_list2txt(self):
        """
        将ip_list以增加的形式写入到txt文本中

        :return:None
        """
        for ip in self.ip_list:
            with open("ip_list_https.txt", "a", encoding="utf-8") as f:
                f.write(ip[0] + " " + ip[1] + "\n")

    def get_ip_list_from_txt(self):
        """
        从txt文本中读取ip_list

        :return: None
        """
        with open("ip_list_https.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                ip_t = line.strip("\n").split(" ")
                self.ip_list.append((ip_t[0], ip_t[1]))

    def __get_random_ip(self):
        """
        :return: 1.http还是https 2.ip
        """
        random_one = random.choice(self.ip_list)
        return random_one[0].lower(), random_one[1]

    def is_ip_useful(self,ip):
        try:
            url = "http://www.baidu.com/"
            proxies = {ip[0]: ip[1]}
            # 空白位置为测试代理ip和代理ip使用端口
            headers = {"User-Agent": "Mozilla/5.0"}
            # 响应头
            res = requests.get(url, proxies=proxies, headers=headers)
            # 发起请求
            # print(res.status_code)  # 返回响应码
        except Exception as e:
            print(e)
            return False
        return res.status_code ==200

    def get_a_useful_ip(self):
        ip = self.__get_random_ip()

        while not self.is_ip_useful(ip):
            ip = self.__get_random_ip()
        return ip
