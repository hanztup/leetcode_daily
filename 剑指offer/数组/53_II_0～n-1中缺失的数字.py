# coding:utf-8

'''
date: 2021/5/10
content:
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8

限制：
1 <= 数组长度 <= 10000
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        解法一：二分法
        '''
        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start <= end:
            mid = (end - start) // 2 + start
            if nums[mid] <= mid:
                start = mid + 1
            elif nums[mid] > mid:
                end = mid - 1

        return start


if __name__ == '__main__':
    s = Solution()
    result = s.missingNumber([0,1,2,3,4,5,6,7,9])
    print(result)