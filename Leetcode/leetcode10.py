# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s) + 1 # 行数，s
        m = len(p) + 1 # 列数，p

        dp = [[False] * m for _ in range(n)]
        dp[0][0] = True
        for i in range(1,n):
            dp[i][0] = False

        for i in range(2,m):
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'

        for i in range(1, n):
            for j in range(1, m):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1]=='.')
                else:
                    dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2]=='.'))
        return dp[-1][-1]






if __name__ == '__main__':
    print(Solution().isMatch('aaa', 'a*a'))
