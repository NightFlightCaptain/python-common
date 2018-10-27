# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        从中间依次往两边延伸
        '''
        # l = len(s)
        # olist = [0] * l
        # nlist = [0] * l
        # longestSubStr = ""
        # longestLen = 0
        # for j in range(l):
        #     for i in range(j + 1):
        #         if j - i <= 1:
        #             if s[i] == s[j]:
        #                 nlist[i] = 1
        #                 if (j-i+1) > longestLen:
        #                     longestLen = j-i+1
        #                     longestSubStr = s[i:j+1]
        #         else:
        #             if olist[i+1] == 1 and s[i] == s[j]:
        #                 nlist[i] = 1
        #                 if (j-i+1) > longestLen:
        #                     longestLen = j-i+1
        #                     longestSubStr = s[i:j+1]
        #     olist = nlist
        #     nlist = [0] * l
        # return longestSubStr


        if len(s) <2 or s==s[::-1]:
            return s

        l = len(s)
        start =0
        longestLen = 1
        for i in range(1,l):
            odd = s[i-longestLen-1:i+1]
            even = s[i-longestLen:i+1]
            if i-longestLen > 0 and odd == odd[::-1]:
                start = i-longestLen -1
                longestLen+=2
            elif i-longestLen >=0 and even == even[::-1]:
                start = i -longestLen
                longestLen+=1
        return s[start:start+longestLen]


if __name__ == '__main__':
    print(Solution().longestPalindrome("abbbacdfdgfsdbb"))
