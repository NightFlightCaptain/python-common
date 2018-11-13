# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

def shell_sort(input_list):
    length = len(input_list)
    if length <=0:
        return input_list
    sorted_list = input_list
    gap = length//2
    while gap >0:
        for i in range(gap,length):
            temp = sorted_list[i]
            j = i-gap
            while j >=0 and sorted_list[j] > temp:
                sorted_list[j+gap] = sorted_list[j]
                j-=gap
            sorted_list[j+gap] = temp
        gap//=2
    return sorted_list



if __name__ == '__main__':
    input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
    print("排序前:",input_list)
    print("排序后:",shell_sort(input_list))