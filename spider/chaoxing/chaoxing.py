# -*- coding:utf-8 -*-
# @Time      :2019/12/2 10:25
# @Author    :小栗旬
import json
import re

import os
from bs4 import BeautifulSoup

from spider.spider_tools.Req import Req

header = {
    'Host': 'mooc1-1.chaoxing.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'nested-navigate',
    'Referer': 'https://mooc1-1.chaoxing.com/mycourse/studentstudy?chapterId=167501723&courseId=204962725&clazzid=10078203',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    # 这个地方增加自己的cookie
    'Cookie': '',
}


def get_home_page():
    home_url = "https://mooc1-1.chaoxing.com/mycourse/studentstudycourselist?courseId=204962725&chapterId=167501723&clazzid=10078203"

    response = Req.get(home_url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    hrefs_box = soup.find_all('div', attrs={'class': 'ncells'})

    for href in hrefs_box:
        text = href.find('a').attrs['href']
        pattern = re.compile(r"javascript:getTeacherAjax[(]'204962725','10078203','(.*?)'[)];",
                             re.MULTILINE | re.DOTALL)
        index = re.search(pattern, text)
        know_id = index.group(1)
        get_chapter_page(know_id)


def get_chapter_page(know_id):
    url = 'https://mooc1-1.chaoxing.com/knowledge/cards?clazzid=10078203&courseid=204962725&knowledgeid=' + str(know_id)
    response = Req.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.find_all('script')[4].get_text()
    pattern = re.compile(r'"objectid":"(.*?)"')
    index = re.search(pattern, text)
    if index is not None:
        object_id = index.group(1)
        print(object_id)
        download_pdf(object_id)


def download_pdf(object_id):
    url = "https://mooc1-1.chaoxing.com/ananas/status/" + object_id
    response = Req.get(url)
    data = json.loads(response.text)
    pdf_url = data.get("pdf")
    if pdf_url is not None:
        pdf_name = data.get("filename")
        save_pdf(pdf_url, pdf_name)


def save_pdf(pdf_url, file_name, file_path='D:\\'):
    html = Req.get(pdf_url)
    # 获取pdf的后缀名
    file_suffix = os.path.splitext(pdf_url)[1]
    with open(file_path + file_name + file_suffix, 'wb')as file:
        file.write(html.content)
    print("下载{}成功".format(file_name))


if __name__ == '__main__':
    get_home_page()
