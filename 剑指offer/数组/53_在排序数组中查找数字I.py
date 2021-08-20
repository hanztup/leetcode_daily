# coding:utf-8

'''
date: 2021/5/10
content:

统计一个数字在排序数组中出现的次数。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: 2

示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: 0


限制：
0 <= 数组长度 <= 50000

注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return 0

        '''
        method 1: 直接for循环
        '''
        # times = 0
        # for i in range(len(nums)):
        #     if nums[i] > target:
        #         break
        #
        #     if nums[i] == target:
        #         times += 1
        # return times


        '''
        method 2: 第一种二分法，分别找左边界和右边界
        '''
        # left, right = 0, len(nums) - 1
        #
        # # find right edge
        # start, end = 0, len(nums) - 1
        # while start <= end:
        #     mid = (end - start) // 2 + start
        #     if nums[mid] <= target:
        #         start = mid + 1
        #     else:
        #         end = mid - 1
        # right = start
        #
        # # find left edge
        # start, end = 0, len(nums) - 1
        # while start <= end:
        #     mid = (end - start) // 2 + start
        #     if nums[mid] >= target:
        #         end = mid - 1
        #     else:
        #         start = mid + 1
        # left = end
        #
        # return right - left - 1


        '''
        method 3: 二分法，利用查找插入位置的思路
        '''

        def helper(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (end - start) // 2 + start
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return start

        return helper(nums, target) - helper(nums, target - 1)















