# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


def bubble_sort(input_list):
    """
    冒泡排序

    :param input_list:
    :return:
    """
    if len(input_list) <=0:
        return input_list
    sorted_list = input_list
    for i in range(len(sorted_list)-1):
        isChanged = False
        for j in range(len(sorted_list)-1-i):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j+1],sorted_list[j] =sorted_list[j],sorted_list[j+1]
                isChanged = True
        if not isChanged:
            break
    return sorted_list

if __name__ =='__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print(bubble_sort(input_list))
    print(bubble_sort([-2,-45,-6]))
    print(bubble_sort([]))