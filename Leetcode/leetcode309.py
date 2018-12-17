# -*- coding:utf-8 -*-
# @Time      :2018/12/13 14:28
# @Author    :wanhaoran
# @FileName  :leetcode309.py


"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]


与leetcode188有所关联
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        notown,own,cool = 0,float('-inf'),float('-inf')
        for price in prices:
            notown,own,cool = max(notown,cool),max(own,notown-price),own+price
        return max(notown,cool)
#

if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit([1, 3, 6, 7, 9, 4, 10, 5, 6])
    print(result)