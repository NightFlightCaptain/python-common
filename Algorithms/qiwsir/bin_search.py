# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

from bisect import *

"""
二分查找
list.index()无法应对大规模数据的查询，需要用其它方法解决，这里谈的就是二分查找
#思路说明
在查找方面，python中有list.index()的方法。例如：
    >>> a=[2,4,1,9,3]           #list可以是无序，也可以是有序
    >>> a.index(4)              #找到后返回该值在list中的位置
    1
    >>> a.index(5)              #如果没有该值，则报错
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: 5 is not in list
这是python中基本的查找方法，虽然简单，但是，如果由于其时间复杂度为O(n)，对于大规模的查询恐怕是不足以胜任的。二分查找就是一种替代方法。
二分查找的对象是：有序数组。这点特别需要注意。要把数组排好序先。怎么排序，可以参看我这里多篇排序问题的文章。
基本步骤：
1. 从数组的中间元素开始，如果中间元素正好是要查找的元素，则搜素过程结束；
2. 如果某一特定元素大于或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开始一样从中间元素开始比较。
3. 如果在某一步骤数组为空，则代表找不到。
这种搜索算法每一次比较都使搜索范围缩小一半。时间复杂度：O(logn)
"""

def bin_search(list,num,left,right):
    if left > right:
        return left
    mid = left + (right-left)//2
    if list[mid] == num:
        return mid
    elif list[mid] < num:
        left = mid+1
    else:
        right = mid-1
    return bin_search(list,num,left,right)

def search(list,num):
    left = 0
    right = len(list)-1
    return bin_search(list,num,left,right)


"""
对于python，不能忽视其强大的标准库。经查阅，发现标准库中就有一个模块，名为：bisect。其文档中有这样一句话：
>>This module provides support for maintaining a list in sorted order without having to sort the list after each insertion. For long lists of items with expensive comparison operations, this can be an improvement over the more common approach. The module is called bisect because it uses a basic bisection algorithm to do its work. The source code may be most useful as a working example of the algorithm (the boundary conditions are already right!).

这段话的关键点是在说明：
- 模块接受排序后的列表。
- 本模块同样适用于长列表项。因为它就是用二分查找方法实现的，有兴趣可以看其源码（源码是一个很好的二分查找算法的例子，特别是很好地解决了边界条件极端的问题.)
-关于本模块，可以查看官方文档：https://docs.python.org/2/library/bisect.html
"""


def bisectSearch(list,num):
    i = bisect_left(list,num)
    return i


if __name__ == '__main__':
    # print(search([1,9,16,92,154,7777,65223],7778))
    print(bisectSearch([1,9,16,92,154,7777,65223],7776))