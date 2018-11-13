# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

def select_sort(input_list):
    length = len(input_list)
    if length<=0:
        return input_list
    sorted_list = input_list

    for i in range(length):
        min_position = i
        for j in range(i+1,length):
            if sorted_list[j] < sorted_list[min_position]:
                min_position = j
        sorted_list[i],sorted_list[min_position] = sorted_list[min_position],sorted_list[i]
    return sorted_list

if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print(input_list)
    print(select_sort(input_list))