# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


"""
对于大整数计算，一般都要用某种方法转化，否则会溢出。但是python无此担忧了。
Python支持“无限精度”的整数，一般情况下不用考虑整数溢出的问题，而且Python Int 整数类型与任意精度的Long整数类可以无缝转换，超过Int 范围的情况都将转换成Long类型。
注意：前面的“无限精度”是有引号的。事实上也是有限制的，对于32位的机器，其上限是：2^32-1。真的足够大了。
为什么Python能够做到呢？请有兴趣刨根问底的去看Python的有关源码。本文不赘述。

"""


def str2list4int(string):
    nums = [int(i) for i in string]
    nums.reverse()
    return nums


def list2str(list):
    return "".join(str(i) for i in list)


def multiplication(str1,str2):
    p=int(str1)*int(str2)
    print(p)
    if len(str1) < len(str2):
        str1,str2 = str2,str1
    list1 = str2list4int(str1)
    list2 = str2list4int(str2)
    list_result = [0 for i in range(len(str1)+len(str2))]

    # 简单理解版本
    # for i in range(len(str1)):
    #     for j in range(len(str2)):
    #         list_result[i+j] += list1[i] * list2[j]
    #
    # for i in range(len(list_result)):
    #     if list_result[i] > 9:
    #         list_result[i+1] += list_result[i]//10
    #         list_result[i] = list_result[i] %10

    for i in range(len(str1)):
        for j in range(len(str2)):
            current = list1[i] * list2[j]
            k=0
            while current>0:
                current+=list_result[i+j+k]
                list_result[i+j+k] = current%10
                current//=10
                k+=1

    list_result.reverse()
    return list2str(list_result)


if __name__=="__main__":
    print(multiplication("4671414575","495445214242145422"))

