# -*- coding:utf-8 -*-
# @Time      :2018/12/8 0:37
# @Author    :wanhaoran
# @FileName  :vx_vote_simple.py

import random
import re
import string
import time

import requests




ip= "218.17.139.5:808"


def random_sleep_time(digits_length):
    digits_char = string.digits
    need_sleep_time = ''
    for i in range(digits_length):
        need_sleep_time += random.choice(digits_char)
    return int(need_sleep_time) + 1


def getRandomString(id_length):
    charSeq = string.ascii_letters + string.digits
    randString = ''
    for i in range(id_length):
        randString += random.choice(charSeq)
    return randString


def get_open_id():
    return getRandomString(16) + "-" + getRandomString(11)


def get_ip():
    ip_list = [
        "182.96.249.68:808",
        "218.17.139.5:808",
        "60.191.201.38:45461"
    ]

def success(open_id):
    url = "http://web.weitou99.com/index/vote/success"

    proxy = {
        "http": ip
    }

    activityId="26879"
    playerId="2094978"
    number="15"
    activityName="享新鲜 悦美味--寻找武汉最健康生鲜（A赛区）"
    openId=open_id
    isGift="1"

    params = {
        "activityId": activityId,
        "openId": openId,
        "playerId": playerId,
        "number": number,
        "activityName": activityName,
        "isGift": isGift
    }

    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        # "Connection": "keep-alive",
        # "Host": "web.weitou99.com",
        # "Cookie": "JSESSIONID=BEDA66485B52B1FB4C916C39499EA081",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; U;  zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger"
    }

    # params = parse.urlencode(params)
    # print(params)
    r = requests.get(url=url, params=params, headers=headers, proxies=proxy)
    html = r.text
    # soup = BeautifulSoup(html,"html.parser")
    pattern1 = re.compile(r'var _0sdfad="(.*?)"', re.MULTILINE | re.DOTALL)
    pattern2 = re.compile(r'var _0ees88="(.*?)"', re.MULTILINE | re.DOTALL)
    index1 = re.search(pattern1, html)
    index2 = re.search(pattern2, html)
    res1 = index1.group().replace(r'var _0sdfad="', "").replace('"', '')
    res2 = index2.group().replace(r'var _0ees88="', "").replace('"', '')
    # print(soup)
    return res1, res2

    # request = urllib.request.Request(url=url, params=params,headers=headers)
    # response = urllib.request.urlopen(request, timeout=300)
    # data = response.read().decode("UTF-8")

    # div_bf = BeautifulSoup(data,"lxml")
    # div = div_bf.find_all('div', class_='panel-body')
    # a_bf = BeautifulSoup(str(div[0]),"lxml")
    # response_text=a_bf.find("p").text
    # print("使用的openId: "+open_id+"  投票结果: "+response_text)


def vote_real(open_id):
    index1, index2 = success(open_id=open_id)
    print("param1: ", index1, " param2: ", index2)
    url = "http://web.weitou99.com/index/" + index2 + "/" + index1
    # print(url)

    proxy = {
        "https": ip
    }

    activityId = "26879"
    playerId = "2094978"
    number = "15"
    activityName = "享新鲜 悦美味--寻找武汉最健康生鲜（A赛区）"
    openId = open_id
    isGift = "1"

    params = {
        "activityId": activityId,
        "openId": openId,
        "playerId": playerId
    }

    headers = {
        # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        # "Connection": "keep-alive",
        # "Host": "web.weitou99.com",
        # "Cookie": "JSESSIONID=BEDA66485B52B1FB4C916C39499EA081",
        # "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Linux; U;  zh-cn; GT-S5660 Build/GINGERBREAD) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1 MicroMessenger"
    }
    r = requests.post(url=url, params=params, headers=headers, proxies=proxy)
    print(r)


def do():
    # true_open_id = "&openId=o3fcT1nTBe9AFXUP-Ats9kMcpd3K"

    open_id = get_open_id()
    # print(open_id)
    vote_real(open_id)


if __name__ == "__main__":
    success_count = 0
    error_count = 0
    for i in range(2000):
        try:
            do()
            random_wait_time = random_sleep_time(1)
            time.sleep(random_wait_time)
        except Exception:
            error_count+=1
            print("发生了一个异常:error_count=",error_count)
        else:
            success_count+=1
            print("成功执行了一个",success_count)