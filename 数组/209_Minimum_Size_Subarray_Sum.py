# coding:utf-8

'''
date: 2021/2/4
content:

给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

 

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
 

进阶：

如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。

'''

import sys

class Solution(object):
    def minSubArrayLen1(self, target, nums):
        """
        时间复杂度O(n)的做法
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        result = sys.maxsize
        sum_val = 0
        start = 0

        for end in range(len(nums)):
            sum_val += nums[end]

            while sum_val >= target:
                sub_length = end - start + 1
                result = result if result < sub_length else sub_length
                sum_val -= nums[start]
                start += 1

        return result if result != sys.maxsize else 0




if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen1(7, [2,3,1,2,4,3]))
