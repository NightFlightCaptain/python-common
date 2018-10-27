# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        '''
        暴力法，按照顺序排列，再读取
        '''
        if numRows ==1:
            return s
        slist = ['']*numRows

        add_or_delete = 1
        # 当前行数
        curRow = 0
        for i in range(0,len(s)):
            slist[curRow]+=s[i]
            curRow += add_or_delete
            # 到最上层或者最下层是掉头
            if curRow ==numRows-1 or curRow ==0:
                add_or_delete*=-1

        sl=""
        print(slist)
        for i in range(numRows):
            sl+=slist[i]

        return sl




if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING",4))