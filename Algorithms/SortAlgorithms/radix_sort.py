# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

def radix_sort(input_list):
    """
    基数排序，按照每一位进行排序，首先按个位数大小进行排序，然后按照十位大小进行排序（没有十位则认为是0）
    :param input_list:
    :return:
    """
    max_bit = maxbit(input_list)
    for i in range(1,max_bit+1):
        input_list.sort(key=lambda x:digit(x,i))
        print('按',i,'位排序后',input_list)
    return input_list


def maxbit(input_list):
    maxLen = 0
    for i in input_list:
        maxLen = max(maxLen,len(str(i)))
    return maxLen

def digit(num,d):
    num = num //(10**(d-1))
    num = num%10
    return num


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print(maxbit(input_list))
    print('原始：', input_list)
    radix_sort(input_list)
    print('最终：', input_list)