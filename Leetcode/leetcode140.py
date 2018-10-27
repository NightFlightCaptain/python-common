# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.helper(s,wordDict,{})

    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []

        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

        # l = len(s)
        # dp = [0] * (l + 1)
        # dp[0] =1
        # for i in range(1, l + 1):
        #     for j in range(len(wordDict)):
        #         if i >= len(wordDict[j]) and dp[i - len(wordDict[j])] and s[i - len(wordDict[j]):i] == wordDict[j]:
        #             dp[i] = 1
        # if dp[-1] !=1:
        #     return []
        #
        # resultList = []
        # list = []
        # string = ""
        # self.backtrack(string, list, resultList, s, wordDict)
        # return resultList

    def backtrack(self, string, list, resultlist, s, wordDict):
        # print("string:",string)
        # print(list)
        if string == s:
            resultlist.append(' '.join(list))
        elif len(string) >= len(s):
            return
        elif string == s[0:len(string)]:
            for i in range(len(wordDict)):
                list.append(wordDict[i])
                self.backtrack(string + wordDict[i], list, resultlist, s, wordDict)
                del (list[-1])


if __name__ == '__main__':
    print(Solution().wordBreak("pineapplepenapple",
                               ["apple", "pen", "applepen", "pine", "pineapple"]))

