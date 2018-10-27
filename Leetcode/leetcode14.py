# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # l =len(strs)
        # if l == 0:
        #     return ''
        # if l == 1:
        #     return strs[0]
        #
        # strs= sorted(strs, key=lambda x:len(x))
        # result = ''
        # for j in range(len(strs[0])):
        #     i=1
        #     while i<l and strs[i][j] == strs[0][j]:
        #         i+=1
        #     if i == l:
        #         result+=strs[0][j]
        #     else:
        #         break
        # return result

        l =len(strs)
        if l == 0:
            return ''
        if l == 1:
            return strs[0]

        strs= sorted(strs, key=lambda x:len(x))
        result = strs[0]
        for j in range(len(strs[0])):
            i=1
            while i<l and strs[i].startswith(result):
                i+=1
            if i != l:
                result=result[0:-1]
            else:
                break
        return result


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["ab", 'aa']))