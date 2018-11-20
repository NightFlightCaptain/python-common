# -*- coding:utf-8 -*-
# @Time      :2018/11/20 13:56
# @Author    :wanhaoran
# @FileName  :leetcode91.py

"""
一条包含字母 A-Z 的消息通过以下方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
给定一个只包含数字的非空字符串，请计算解码方法的总数。

示例 1:

输入: "12"
输出: 2
解释: 它可以解码为 "AB"（1 2）或者 "L"（12）。
示例 2:

输入: "226"
输出: 3
解释: 它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
"""

class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """


        if not s or len(s) == 0:
            return 0
        if s[0]=='0':
            return 0
        if len(s)==1 and s[0]!='0':
            return 1
        dp = [0] *(len(s)+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(1,len(s)):
            if s[i]!='0':
                dp[i+1] += dp[i]
            if 10<= int(s[i-1:i+1]) <=26:
                dp[i+1]+=dp[i-1]
        return dp[-1]

        # length = len(s)
        # cnt = [1] *(length+1)
        # if s[0]=='0':
        #     cnt[1] = 0
        # for i in range(1,length):
        #     t1 = 0 if s[i]=='0' else cnt[i]
        #     t2 = cnt[i-1] if 10<=int(s[i-1:i+1])<=26 else 0
        #     cnt[i+1]=t1+t2
        # return cnt[-1]

if __name__ == '__main__':
    print(Solution().numDecodings("10"))