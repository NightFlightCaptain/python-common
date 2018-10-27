# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    list1 = ListNode(1)

    list2 = ListNode(9)

    # list1.next = list2
    # list1 = list1.next

    # list1.next = list1 = list2

    # list1.next = list1
    # list1 = list2
    list1 = list1.next = list2

    while list1:
        print(list1.val)
        list1 = list1.next
