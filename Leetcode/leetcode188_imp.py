# -*- coding:utf-8 -*-
# @Time      :2018/11/21 23:14
# @Author    :wanhaoran
# @FileName  :leetcode188_imp.py

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
示例 2:

输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""

class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices)==0:
            return 0
        if k>= len(prices)//2:
            # res = 0
            # for i in range(1,len(prices)):
            #     res+=prices[i]-prices[i-1] if prices[i]-prices[i-1]>0 else 0
            # return res
            # 一种写法
            return sum([prices[i]-prices[i-1] if prices[i]>prices[i-1] else 0 for i in range(1,len(prices))])

        dp = [[0] * len(prices) for i in range(k+1)]
        tmp = [-prices[0]] * (k+1)
        for m in range(1,k+1):
            for i in range(1,len(prices)):
                tmp[m]=max(tmp[m],dp[m-1][i-1]-prices[i])
                dp[m][i] = max(tmp[m]+prices[i],dp[m][i-1])
        return dp[-1][-1]




if __name__ == '__main__':
    solution = Solution()
    result = solution.maxProfit(2,[3,3,5,0,0,3,1,4])
    print(result)
    result = solution.maxProfit(2,[0,1,2,3,4])
    print(result)
    result = solution.maxProfit(2,[7,6,4,3,1])
    print(result)
