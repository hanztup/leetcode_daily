# coding:utf-8

'''
date: 2021/4/25
content:
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

限制：
2 <= n <= 100000
'''

class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return -1

        '''解法一: hash map, 时间复杂度：O(n), 空间复杂度：O(n)'''
        visited = {}
        for num in nums:
            if num not in visited:
                visited[num] = 1
            else:
                return num

        '''（待补充）解法二: sort, 时间复杂度：O(nlogn) ~ O(n^2), 空间复杂度：O(1)'''


        '''解法三：原地置换, 时间复杂度：O(n), 空间复杂度：O(1)'''
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue

            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


