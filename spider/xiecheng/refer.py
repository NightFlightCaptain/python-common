# -*- coding:utf-8 -*-
# @Time      :2019/1/2 23:46
# @Author    :小栗旬


""" Created on Mon Aug 7 21:05:03 2017 @author: Administrator """
import urllib.request
from bs4 import BeautifulSoup
import pymysql.cursors

''' 目标:获取酒店名称和酒店星级 '''
url1 = 'http://hotels.ctrip.com/hotel/435383.html'
html1 = urllib.request.urlopen(url1).read().decode(
    'utf-8')
# 1.
# 获取酒店名称信息
soup1 = BeautifulSoup(html1, 'lxml')
result1 = soup1.find_all(attrs={"itemprop": "name"})
hotelName = result1[0].string
print("酒店名称为:{}".format(hotelName))
# 2.
# 获取酒店星级信息
soup12 = BeautifulSoup(html1, 'lxml')
result12 = soup12.find_all(attrs={"class": "grade"})
print(result1)
result12 = str(result12)
soup13 = BeautifulSoup(result12, 'lxml')
result13 = soup13.find_all('span')
hotelStar = result13[0]['title']
print("酒店星级为:{}".format(hotelStar))
''' 目标:获取酒店最低房价和评论总数 '''
url2 = "http://m.ctrip.com/html5/hotel/HotelDetail/435383.html"
html2 = urllib.request.urlopen(url2).read().decode('utf-8')
# 获取酒店最低价
soup2 = BeautifulSoup(html2, 'lxml')
result2 = soup2.find_all(attrs={"class": "js-cas-p"})
lowPrice = result2[0]['data-cas-p']
print("酒店最低房价为:{}".format(lowPrice))
# 评论总数
result21 = soup2.find_all(attrs={"class": "dt-color12 dt-fn15"})
commentCounts = result21[0].string
print("评论总数为:{}".format(commentCounts))
''' 目标:获取酒店卫生评分、环境评分、服务评分、设施评分、用户推荐比、用户评分、评价内容 '''
url3 = 'http://m.ctrip.com/html5/hotel/HotelDetail/dianping/435383.html'
html3 = urllib.request.urlopen(url3).read().decode('utf-8')
soup3 = BeautifulSoup(html3, 'lxml')
# 获取酒店各项评分数据
result32 = soup3.find_all(attrs={"class": "ve-txt"})
result32 = str(result32)
soup32 = BeautifulSoup(result32, 'lxml')
result33 = soup32.find_all('em')
userRecommendRate = result33[0].string
hRating = result33[1].string
eRating = result33[2].string
sRating = result33[3].string
iRating = result33[4].string
print("用户推荐为:{}".format(userRecommendRate))
print("卫生评分为:{}分".format(hRating))
print("环境评分为:{}分".format(eRating))
print("服务评分为:{}分".format(sRating))
print("设施评分为:{}分".format(iRating))
# 提取用户评论数据
result34 = soup3.find_all(attrs={"class": "hotel-cell-num"})
result34 = str(result34[1])
soup33 = BeautifulSoup(result34, 'lxml')
result35 = soup33.find_all('p')
for i in range(0, 10): userName = result35[i].get_text()
result36 = soup3.find_all(attrs={"itemprop": "datePublished"})
datePublished = result36[i].string
print("评论发表于:{}".format(datePublished))
result37 = soup3.find_all(attrs={"itemprop": "ratingValue"})
userRating = result37[i].string
print("评分为:{}".format(userRating))
result38 = soup3.find_all(attrs={"class": "tree-ellips-line6 js_arr"})
commentText = result38[i].get_text()
print("评论内容为:{}".format(commentText))
''' 数据库操作 '''
# 获取数据库链接
connection = pymysql.connect(host='localhost', user='root', password='123456', db='xiecheng', charset='utf8mb4')
try:
    with connection.cursor() as cursor:
        sql = "insert into `macro-polo` (`hotelName`,`hotelStar`,`lowPrice`,`commentCounts`,`userRecommendRate`,`hRating`,`eRating`,`sRating`,`iRating`,`datePublished`,`userRating`,`commentText`) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (
            hotelName, hotelStar, lowPrice, commentCounts, userRecommendRate, hRating, eRating, sRating, iRating,
            datePublished,
            userRating, commentText))
    connection.commit()
finally:
    connection.close()