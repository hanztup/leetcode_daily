# coding:utf-8

'''
date: 2021/5/23
content:
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。


示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]


提示：
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        '''
        解法一
        思路：
        时间复杂度：
        空间复杂度：
        '''

        nums.sort()
        res, k = [], 0

        for k in range(len(nums) -2):
            if nums[k] > 0:
                break

            if k > 0 and nums[k] == nums[k-1]:
                continue

            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1

                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1
                        print(j)

                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
                    while i < j and nums[j] == nums[j+1]:
                        j -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    ret = s.threeSum([-1,0,1,2,-1,-4])
    print(ret)




