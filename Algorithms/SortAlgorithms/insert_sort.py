# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


def insert_sort(input_list):
    """
    插入排序，从第二个数开始依次和前面的数比较。每比较一下，要么交换，要么跳出内存循环，然后将这个数赋值给当前位置的数

    :param input_list:
    :return:
    """
    length = len(input_list)
    if length <= 0:
        return input_list
    sorted_list = input_list

    for i in range(1, length):
        temp = sorted_list[i]
        j = i - 1
        while j >= 0 and sorted_list[j] > temp:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = temp
    return sorted_list


def binary_search(input_list, end, value):
    left = 0
    right = end - 1
    while left < right:
        middle = left + (right - left) // 2
        if input_list[middle] > value:
            right = middle - 1
        elif input_list[middle] < value:
            left = middle + 1
        else:
            return middle
    return left


def binary_insert_sort(input_list):
    length = len(input_list)
    if length <= 0:
        return input_list
    sorted_list = input_list

    for i in range(1, length):
        temp = sorted_list[i]
        j = i - 1
        insert_index = binary_search(input_list,i,sorted_list[i])
        while j>=insert_index:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = temp
    return sorted_list

    # sorted_list = input_list
    # for i in range(len(sorted_list)):
    #     minNum = sorted_list[i]
    #     for j in range(i+1,len(sorted_list)):
    #         if sorted_list[j] < minNum:
    #             minNum = sorted_list[j]
    #             position = j
    #     sorted_list[i],sorted_list[position] = minNum,sorted_list[i]
    # return sorted_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print(insert_sort(input_list))
    print(binary_insert_sort(input_list))
    print(insert_sort([-2, -45, -6]))
    print(insert_sort([]))
