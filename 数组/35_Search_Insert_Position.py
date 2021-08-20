# coding:utf-8

'''
date: 2021/2/2
content:

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 特殊情况处理
        if not nums:
            return 0

        if target < nums[0]:
            return 0

        if target > nums[-1]:
            return len(nums)


        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid

        return right

'''
感受：
这道题最让人难以捉摸的就是边界问题。关注三个位置的边界：
1. 49行的right取的是左闭右开区间
2. 51行对应也要取左闭右开区间
3. 54和56行也要对应区间


同时要注意两个细节：
1. 计算中间mid值时，采用left + (right - left) // 2, 而不用(left+right) // 2. (因为left + right有一定风险导致溢出，但python中倒不用在意) 
2. 60行要能够分析为什么取右端点
'''