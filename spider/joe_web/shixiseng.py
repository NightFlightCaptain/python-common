# -*- coding:utf-8 -*-
# @Time      :2019/2/22 17:22
# @Author    :小栗旬
import csv
import warnings

from bs4 import BeautifulSoup

from spider.spider_tools.Req import Req

warnings.filterwarnings('ignore')


def get_offer_list(param, page):
    csv_headers = ['job_name',
                   'job_city',
                   'job_com_name',
                   'job_time_month',
                   'job_money',
                   'job_week',
                   'job_good',
                   'job_com_position',
                   'job_detail']

    write_csv_header(csv_headers)
    for i in range(1, page + 1):
        one_page = get_one_page(param, i)

        hrefs = get_hrefs(one_page)
        for href in hrefs:
            detail_page = get_detail_page(href)
            job_detail = get_detail_job(detail_page)
            if job_detail is None:
                continue
            write_csv_rows(csv_headers, job_detail)


def get_one_page(keyword, page):
    index_url = "https://www.shixiseng.com/interns/st-intern_c-420100_?k=" + keyword + "&p="

    index_full_url = index_url + str(page)

    response = Req.get(index_full_url)

    if response.status_code == 200:
        return response.text


def get_hrefs(text):
    hrefs_list = []
    soup = BeautifulSoup(text, "html.parser")
    hrefs_box = soup.find_all('div', attrs={'class': 'name-box clearfix'})
    for href in hrefs_box:
        url = href.find('a').attrs['href']
        hrefs_list.append(url)
    return hrefs_list


def get_detail_page(weburl):
    detail_url = "https://www.shixiseng.com" + weburl

    response = Req.get(detail_url)
    if response.status_code == 200:
        return response.text
    return None


def has_word(text):
    words = ["c++", "前端", "php", "PHP", "C++", "安卓", "嵌入式", "IOS", "游戏"]
    for word in words:
        if word in text:
            return True
    return False


def decrypt_text(text):
    """
    对数字进行解密
    :param text:
    :return:
    """
    mapping = {
        "&#xebb8": "0",
        "&#xef37": "1",
        "&#xede1": "2",
        "&#xf8f3": "3",
        "&#xf7cf": "4",
        "&#xf134": "5",
        "&#xf819": "6",
        "&#xefec": "7",
        "&#xec4c": "8",
        "&#xf125": "9"
    }

    for key, value in mapping.items():
        text = text.replace(key, value)
    return text


def get_detail_job(text):
    text = decrypt_text(text)

    soup = BeautifulSoup(text, 'lxml')

    job_name = soup.find('div', attrs={'class': 'new_job_name'}).get_text().rstrip()
    if has_word(job_name):
        return None
    job_city = soup.find('span', attrs={'class': 'job_position'}).string
    job_time_month = soup.find('span', attrs={'class': 'job_time cutom_font'}).get_text()
    job_money = soup.find('span', attrs={'class': 'job_money cutom_font'}).get_text()

    job_week = soup.find('span', attrs={'class': 'job_week cutom_font'}).get_text()
    job_good = soup.find('div', attrs={'class': 'job_good'}).get_text()
    job_detail = soup.find('div', attrs={'class': 'job_detail'}).get_text().strip().replace("\n", "")
    job_com_name = soup.find('div', attrs={'class': 'job_com_name'}).get_text()
    job_com_position = soup.find('span', attrs={'class': 'com_position'}).get_text()

    job_map = {
        'job_name': job_name,
        'job_city': job_city,
        'job_com_name': job_com_name,
        'job_time_month': job_time_month,
        'job_money': job_money,
        'job_week': job_week,
        'job_good': job_good,
        'job_com_position': job_com_position,
        'job_detail': job_detail
    }

    return job_map


def write_csv_header(csv_headers):
    with open("cc.csv", 'w', encoding='utf-8-sig', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writeheader()


def write_csv_rows(csv_headers, rows):
    with open("cc.csv", 'a', encoding='UTF-8', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writerow(rows)


if __name__ == "__main__":
    get_offer_list("开发", 5)
