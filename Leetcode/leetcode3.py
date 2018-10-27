# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    # 暴力法
    # def allUnique(self, s, start, end):
    #     set = ([])
    #     for i in range(start, end):
    #         if s[i] in set:
    #             return False
    #         else:
    #             set.append(s[i])
    #     return True
    #
    # def lengthOfLongestSubstring(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     ans = 0
    #     set = ([])
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s)+1):
    #             if self.allUnique(s, i, j):
    #                 ans = max(ans, j - i)
    #             else:
    #                 break
    #     return ans

    # set的滑动窗口
    # def lengthOfLongestSubstring(self, s):
    #     set = ([])
    #     ans, i, j = 0, 0, 0
    #     while i < len(s) and j < len(s):
    #         if s[j] not in set:
    #             set.append(s[j])
    #             j += 1
    #             ans = max(ans, j - i)
    #         else:
    #             set.remove(s[i])
    #             i += 1
    #     return ans

    # map的滑动窗口
    def lengthOfLongestSubstring(self, s):
        map = {}
        ans, i= 0, 0
        for j in range(len(s)):
            if s[j] in map:
                i = max(i, map[s[j]]+1)
            map[s[j]] = j
            ans = max(ans, j-i+1)

        return ans

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s="abbcdaa"))
