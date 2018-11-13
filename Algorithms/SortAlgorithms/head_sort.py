# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


def head_sort(input_list):
    length = len(input_list)
    for i in range(length, 0, -1):
        if i == length:
            first_adjust(input_list)
        else:
            adjust(input_list,i)
        print('第',length-i+1,'次排序:',input_list)
        input_list[0],input_list[i-1] = input_list[i-1],input_list[0]
    return input_list


def adjust(input_list,end):
    """
    一次堆排序
    :param input_list:
    :param end:
    :return:
    """
    # length = len(input_list)
    length = end
    for i in range(0,length // 2 , 1):
        if length > 2 * i + 2:
            k = 2 * i + 1 if input_list[2 * i + 1] > input_list[2 * i + 2] else 2 * i + 2
        else:
            k = 2 * i + 1
        if input_list[k] > input_list[i]:
            input_list[k], input_list[i] = input_list[i], input_list[k]


def first_adjust(input_list):
    """
    初始创建堆
    :param input_list:
    :return:
    """
    length = len(input_list)
    for i in range(length // 2 - 1, -1, -1):
        if length > 2 * i + 2:
            k = 2 * i + 1 if input_list[2 * i + 1] > input_list[2 * i + 2] else 2 * i + 2
        else:
            k = 2 * i + 1
        if input_list[k] > input_list[i]:
            input_list[k], input_list[i] = input_list[i], input_list[k]


if __name__ == '__main__':
    input_list = [6, 4, 8, 9, 2, 3, 1]
    print('原始：',input_list)
    head_sort(input_list)
    print('最终：',input_list)

