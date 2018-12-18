# -*- coding:utf-8 -*-
# @Time      :2018/12/14 11:02
# @Author    :wanhaoran
# @FileName  :leetcode322_imp.py

"""
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""

"""
尽量不要使用float('inf')这样的数字，会损耗性能
"""

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        # for i in range(1,amount+1):
        #     dp[0][i] = float('inf')
        #
        #
        # for i in range(1, len(coins) + 1):
        #     for j in range(1, amount + 1):
        #         if j >= coins[i-1]:
        #             dp[i][j] = min(dp[i][j - coins[i-1]] + 1, dp[i-1][j])
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[-1][-1] if dp[-1][-1] != float('inf') else -1

        # dp = [float('inf')] * (amount+1)
        # dp[0]=0
        # for i in range(1,amount + 1):
        #     for coin in coins:
        #         if coin <= i:
        #             dp[i] = min(dp[i], dp[i - coin] + 1)
        # return dp[-1] if dp[-1] !=float('inf') else -1

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[-1] == amount + 1 else dp[-1]

        # dp = [float('inf')] * (amount + 1)
        # coins.sort()
        # dp[0] = 0
        # for i in range(amount + 1):
        #     for coin in coins:
        #         if i + coin <= amount and dp[i + coin] > dp[i] + 1:
        #             dp[i + coin] = dp[i]+1
        # return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    solution = Solution()
    result = solution.coinChange(coins, amount)
    print(result)
