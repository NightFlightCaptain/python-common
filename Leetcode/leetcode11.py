# -*- coding:utf-8 -*-
# __author__ = 'wanhaoran'

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height) - 1
        # short, long = min(height[0], height[l]), max(height[0], height[l])
        left, right = 0, l
        maxA = 0

        for i in range(l, 0, -1):
            maxA = max(maxA, min(height[left] , height[right])*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxA


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
