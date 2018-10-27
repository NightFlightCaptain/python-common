# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        nowCount = 0
        maxCount = 0
        result = 0

        l = len(s)
        if l <=1:
            return 0

        dp = [0]*l
        ans = 0
        for i in range(1, l):
            if s[i] == ')':
                if s[i-dp[i-1] -1] == '(':
                    dp[i] = dp[i-1]+2
                dp[i]+=dp[i-dp[i]]
            ans = max(ans, dp[i])
        return ans



if __name__ == '__main__':
    print(Solution().longestValidParentheses("()(()"))