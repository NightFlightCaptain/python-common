# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

def MergeSort(input_list):
    length = len(input_list)
    if length <= 0:
        return input_list
    merge_sort(input_list, 0, len(input_list) - 1)


def merge_sort(input_list, left, right):
    if left >= right:
        return
    mid = (left+right) // 2  # 如果不能平均，mid为分在左边组
    merge_sort(input_list, left, mid)
    merge_sort(input_list, mid + 1, right)
    merge(input_list, left, mid, right)
    print('从',left,'到',right,'的排序：',input_list)


def merge(input_list, left, mid, right):
    """
    合并从left到right
    :param input_list:
    :param left:
    :param mid:
    :param right:
    :return:
    """
    first_index = left
    secend_index = mid + 1
    sorted_list = []
    while first_index <= mid and secend_index <= right:
        if input_list[first_index] < input_list[secend_index]:
            sorted_list.append(input_list[first_index])
            first_index += 1
        else:
            sorted_list.append(input_list[secend_index])
            secend_index += 1
    if first_index > mid:
        sorted_list.extend(input_list[secend_index :right + 1])
    else:
        sorted_list.extend(input_list[first_index :mid + 1])
    input_list[left:right+1] = sorted_list


if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print('原始：', input_list)
    MergeSort(input_list)
    print('最终：', input_list)
