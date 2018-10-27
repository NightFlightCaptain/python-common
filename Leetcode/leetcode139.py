# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        l = len(s)
        dp = [0] * (l + 1)
        dp[0] =1
        for i in range(1, l + 1):
            for j in range(len(wordDict)):
                if i >= len(wordDict[j]) and dp[i - len(wordDict[j])] and s[i - len(wordDict[j]):i] == wordDict[j]:
                    dp[i] = 1
        return dp[-1]==1


if __name__ == '__main__':
    print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
