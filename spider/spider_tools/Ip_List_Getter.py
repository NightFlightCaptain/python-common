# -*- coding:utf-8 -*-
# @Time      :2019/1/2 16:29
# @Author    :小栗旬

import random

import os
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

    def get_ip_list(self):
        """
        从网站爬取ip_list

        :return:ip_list，数组，元素类型是元祖，元祖第一个元素表示https或http，第二个元素表示ip地址
        """
        for page in range(1, 10):
            url = "http://www.xicidaili.com/nn/" + str(page)
            web_data = requests.get(url=url, headers=self.headers)
            soup = BeautifulSoup(web_data.text, "lxml")
            ips = soup.find_all('tr')
            for i in range(2, len(ips)):
                ip_info = ips[i]
                print(ip_info)
                tds = ip_info.find_all('td')
                self.ip_list.append((tds[5].text, tds[1].text + ":" + tds[2].text))
            self.__write_ip_list2txt()
        return self.ip_list

    def __write_ip_list2txt(self, file_name="ip_list_https.txt"):
        """
        将ip_list以写的形式写入到txt文本中

        :return:None
        """
        with open(os.path.join(os.path.dirname(os.getcwd()), file_name), "w", encoding="utf-8") as f:
            for ip in self.ip_list:
                f.write(ip[0].lower() + " " + ip[1] + "\n")

    def get_ip_list_from_txt(self):
        """
        从txt文本中读取ip_list

        :return: None
        """
        if not os.path.exists(os.path.join(os.path.dirname(os.getcwd()), "useful_ip_list.txt")):
            self.get_ip_list()
        else:
            with open(os.path.join(os.path.dirname(os.getcwd()), "useful_ip_list.txt"), "r") as f:
                lines = f.readlines()
                for line in lines:
                    ip_t = line.strip("\n").split(" ")
                    self.ip_list.append((ip_t[0], ip_t[1]))

    def __get_random_ip(self):
        """
        :return: 1.http还是https 2.ip
        """
        random_one = random.choice(self.ip_list)
        return random_one[0], random_one[1]

    def is_ip_useful(self, ip) -> bool:
        try:
            url = "http://www.baidu.com/"
            proxies = {ip[0]: ip[1]}
            # 空白位置为测试代理ip和代理ip使用端口
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
            # 响应头
            res = requests.get(url, proxies=proxies, headers=headers)
            print("get proxt status code:", res.status_code, res)
            # 发起请求
            # print(res.status_code)  # 返回响应码
        except Exception as e:
            print("test proxy err,", e)
            return False
        return res.status_code == 200

    def get_a_useful_ip(self) -> ():
        """
        从ip_list中获取一个ip，最多循环5次
        :return:
        """
        ip = self.__get_random_ip()

        count = 0
        while count < 5 and not self.is_ip_useful(ip):
            ip = self.__get_random_ip()
            count += 1
        return ip

    def test_all_ip(self, file_name):

        for ip in self.ip_list[::-1]:
            if not self.is_ip_useful(ip):
                self.ip_list.remove(ip)
        self.__write_ip_list2txt(file_name)


if __name__ == '__main__':
    ip = Ip_List_Getter()
    ip.get_ip_list()
    ip.test_all_ip("useful_ip_list.txt")
