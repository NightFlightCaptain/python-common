# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        list =pointList= ListNode(0)

        while True:
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)

            temp = pointList.val
            pointList.val = (l1.val + l2.val + pointList.val) % 10

            if l1.next is None and l2.next is None and l1.val + l2.val + temp< 10:
                break
            else:
                pointList.next=pointList  = ListNode((l1.val + l2.val + temp) // 10)

            l1 = l1.next
            l2 = l2.next
        return list


if __name__ == '__main__':
    pass