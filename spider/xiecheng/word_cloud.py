# -*- coding:utf-8 -*-
# @Time      :2019/1/3 17:53
# @Author    :小栗旬

from wordcloud import WordCloud
import matplotlib.pyplot as plt

def gene():


    font = r'C:\Windows\Fonts\STKAITI.TTF'

    with open(r'D:\Github\python_common\spider\xiecheng\jieba.txt','r',encoding='utf-8') as f:
        sentence = ''
        lines = f.readlines()
        for line in lines:
            sentence+=" "+line+" "
        wordcloud = WordCloud(
            background_color="white",
            width=2000,
            height=1600,
            font_path=font
        ).generate(sentence)

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    wordcloud.to_file('test.png')

if __name__ == '__main__':
    gene()