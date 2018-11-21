# -*- coding:utf-8 -*-
# @Time      :2018/11/21 14:33
# @Author    :wanhaoran
# @FileName  :leetcode95.py


"""
给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。

示例:

输入: 3
输出:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释:
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTrees(start,end):
            res = []
            if end < start:
                res.append(None)
                return res
            for i in range(start,end+1):
                for left_tree in generateTrees(start,i-1):
                    for right_tree in generateTrees(i+1,end):
                        tree = TreeNode(i)
                        tree.left = left_tree
                        tree.right = right_tree
                        res.append(tree)
            return res

        if n <=0:
            return []
        result = generateTrees(1,n)
        return result



if __name__ == '__main__':
    solution = Solution()
    result = solution.generateTrees(0)

    # 树的层序输出
    for i in result:
        stack = []
        stack.append(i)
        while stack.count(None)!=len(stack):
            node = stack.pop(0)
            if node:
                print(node.val,end=" ")
            else:
                print("null",end=" ")
            if node:
                stack.append(node.left)
                stack.append(node.right)
        print()
