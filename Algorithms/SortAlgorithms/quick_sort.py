# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

def quick_sort(input_list,left,right):
    if left <right:
        l = parpation(input_list, left, right)
        quick_sort(input_list,left,l-1)
        quick_sort(input_list,l+1,right)


def parpation(input_list, left, right):
    l,r=left,right
    temp = input_list[left]
    while left < right:
        while right > left and input_list[right] >= temp:
            right -= 1
        input_list[left] = input_list[right]
        while left < right and input_list[left] <= temp:
            left += 1
        input_list[right] = input_list[left]
    input_list[left] = temp
    print(input_list[l:r+1])
    return left

input_list = [11,10,9,8,7,6,5,4,3,2,1]
print(input_list)
quick_sort(input_list,0,len(input_list)-1)
print(input_list)
