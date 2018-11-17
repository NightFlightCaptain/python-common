# -*- coding:utf-8 -*-
# @Time      :2018/11/17 22:53
# @Author    :wanhaoran
# @FileName  :leetcode19.py


"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy= first_point= end_point = ListNode(-1)
        dummy.next = head
        count = 0
        while end_point.next is not None:
            if count <n:
                end_point = end_point.next
                count+=1
            else:
                first_point = first_point.next
                end_point = end_point.next
        first_point.next = first_point.next.next
        return dummy.next

if __name__ == '__main__':
    print(Solution().fourSum([5,5,3,5,1,-5,1,-2],4))