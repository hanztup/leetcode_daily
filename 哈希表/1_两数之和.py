# coding:utf-8

'''
date: 2021/5/23
content:
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。


示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]

示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n^2) 的算法吗？
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        解法一
        思路：两次遍历，第一次遍历用visit存储每个数值，第二次遍历看target - nums[i]是否在visit中
        时间复杂度：O(n)
        空间复杂度：O(n)
        '''

        # # 遍历数组，存储每个数
        # visit = {}
        # for i in range(len(nums)):
        #     visit[nums[i]] = i
        #
        # # 在遍历数组，看每个数所需的数是否在visit中
        # res = []
        # for i in range(len(nums)):
        #     need_remain = target - nums[i]
        #     if (need_remain in visit) and (visit[need_remain] != i):
        #         res.append(i)
        #         res.append(visit[need_remain])
        #         return res
        #
        # return res

        '''
        思路一样，优化一下上述写法，将存储和查找放在一个循环里写
        '''
        visit = {}

        for i, num in enumerate(nums):
            if (target - num) in visit:
                return [visit[target-num], i]
            visit[num] = i
        return []




