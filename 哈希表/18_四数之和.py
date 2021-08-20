# coding:utf-8

'''
date: 2021/5/24
content:

给定一个包含n 个整数的数组nums和一个目标值target，
判断nums中是否存在四个元素 a，b，c和d，
使得a + b + c + d的值与target相等？找出所有满足条件且不重复的四元组。

注意：答案中不可以包含重复的四元组。


示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

示例 2：
输入：nums = [], target = 0
输出：[]

提示：
0 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        '''
        解法一
        思路：将4sum 转换为 遍历 + 3sum。即每次取一个数a，用3sum计算 target - a。
        时间复杂度：O(n^3)
        空间复杂度：O(n)
        '''

        def three_sum(nums, offset, target):
            ret = []
            for k in range(offset+1, len(nums) - 2):
                # if nums[k] > target: break
                if k != (offset + 1) and nums[k] == nums[k-1]: continue

                i, j = k+1, len(nums) - 1
                while i < j:
                    tmp_sum = nums[k] + nums[i] + nums[j]
                    if tmp_sum < target:
                        i += 1
                        while i < j and nums[i] == nums[i-1]: i += 1
                    elif tmp_sum > target:
                        j -= 1
                        while i < j and nums[j] == nums[j+1]: j -= 1
                    else:
                        ret.append([nums[offset], nums[k], nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while i < j and nums[i] == nums[i-1]: i += 1
                        while i < j and nums[j] == nums[j+1]: j -= 1
            return ret


        # 对数组排序
        nums.sort()
        res = []
        visit = {}

        # 转化成遍历 + 3sum
        for l in range(0, len(nums) - 3):
            if nums[l] not in visit:
                visit[nums[l]] = 1
            else:
                continue
            remain_l = target - nums[l]
            res_tmp = three_sum(nums, l, remain_l)
            res.extend(res_tmp)

        return res

if __name__ == '__main__':
    s = Solution()
    result = s.fourSum(nums=[1,0,-1,0,-2,2],
                       target=0)
    print(result)





