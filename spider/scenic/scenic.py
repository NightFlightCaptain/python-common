# -*- coding:utf-8 -*-
# @Time      :2019/10/24 15:23
# @Author    :小栗旬
import csv
import json

import os
from spider.spider_tools.Req import Req


def getScenic():
    url = "https://itrip.meituan.com/volga/api/v1/trip/billboard/list?poiId=761025&billboardId=42&source=mt&inner_source=mtshare&utm_source=appshare&utm_fromapp=qq&lch=appshare_k20koe6yxp6o&ci=57&cityId=57&feclient=lvyou_wap&uuid=AF13A8D6D897C9FB1D61E3438AB054B171041D30F54290C675296FDB636A76F9&client=wap"
    params = {
        "poiId": "761025",
        "output": "json",
        "citylimit": "true",
        "types": "110204",
        "key": "610c2b21dcd0b8b86959bf1478eeac55"
    }
    res = Req.get(url)
    data = json.loads(res.text)
    pois = data.get("data").get("poiList")

    headers = ["name", "introduction", "open_time", "price",
               "suggested_time", "longitude", "latitude",
               "address" ,"phone", "score","photo"]
    write_csv_header(headers)
    for poi in pois:
        map = {
            "name": poi.get("poiName"),
            "introduction": poi.get("recommendBooth"),
            "open_time": "早上8：00-晚上5：00",
            "price": poi.get("price"),
            "suggested_time": "2小时",
            "longitude": poi.get("lng"),
            "latitude": poi.get("lat"),
            "address": poi.get("poiName"),
            "phone": "13063254952",
            "score": poi.get("score"),
            "photo":poi.get("frontImg").replace("/w.h","")+".webp@60q_1l_175w"

        }
        a = str("1").replace("/w.h","")
        print(map)
        write_csv_rows(headers,map)


def write_csv_header(csv_headers):
    with open("cc.csv", 'w', encoding='utf-8-sig', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writeheader()


def write_csv_rows(csv_headers, rows):
    with open("cc.csv", 'a', encoding='UTF-8', newline='') as f:
        f_csv = csv.DictWriter(f, csv_headers)
        f_csv.writerow(rows)


if __name__ == '__main__':
    getScenic()
