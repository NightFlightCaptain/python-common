# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if str is None or len(str) == 0:
            return 0
        result = ''
        if str[0] == '-' or str[0] == '+' or str[0].isdigit():
            result+=str[0]
        else:
            return 0

        for i in range(1, len(str)):
            if str[i].isdigit():
                result+=str[i]
            else:
                break
        if result == '-' or result == '+':
            return 0
        result = int(result)
        if result > 2**31-1:
            return 2**31-1
        if result < -2**31:
            return -2**31
        return result


if __name__ == '__main__':
    print(Solution().myAtoi("-91283472332"))