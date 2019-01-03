# -*- coding:utf-8 -*-
# @Time      :2019/1/3 17:06
# @Author    :小栗旬

import jieba
import os

def do_main(dir_path):
    jieba_comment_list = []
    stopwords = []

    def eachFile(dir_path):
        files = os.listdir(dir_path)
        for file in files[1:50]:
            with open(dir_path+r"/"+file,"r",encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip() == '':
                        continue
                    jieba_comment = jieba.cut(line,HMM=True)
                    jieba_comment_line =" ".join(jieba_comment)
                    jieba_comment_list.append(dele_stopwords(jieba_comment_line))

    def read_stopwords():
        with open("stopWord.txt","r",encoding="utf-8") as stop_file:
            lines = stop_file.readlines()
            for line in lines:
                stopwords.append(line.strip())
        self_stopwords = ["酒店","房间","服务","比较","一个","周围","位置","有点","真的","感觉"]
        stopwords.extend(self_stopwords)


    def dele_stopwords(line):
        word_list = line.split(' ')
        sentence = ''
        for word in word_list:
            word = word.strip()
            if word not in stopwords and word !='\t':
                sentence +=word+" "
        print(sentence.strip())
        return sentence.strip()

    read_stopwords()
    eachFile(dir_path)
    with open("jieba.txt",'w',encoding="utf-8") as wf:
        for jieba_comment in jieba_comment_list:
            wf.write(jieba_comment+"\n")


if __name__ =="__main__":
    do_main(r"D:\Github\python_common\spider\xiecheng\hotel_comment")