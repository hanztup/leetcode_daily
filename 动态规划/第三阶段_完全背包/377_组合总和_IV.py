# coding:utf-8

'''
date: 2021/7/12
content:
给定一个由正整数组成且不存在重复数字的数组，找出和为给定目标正整数的组合的个数。 示例:
nums = [1, 2, 3] target = 4
所有可能的组合为:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。 因此输出为 7。

进阶：如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？
'''


class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，一维dp
        时间复杂度：O(m * n)
        空间复杂度：O(n)
        '''
        dp = [0] * (target + 1)
        dp[0] = 1

        for j in range(target+1):
            for i in range(len(nums)):
                if j < nums[i]:
                    continue
                dp[j] += dp[j - nums[i]]
        print(dp)
        return dp[target]


    '''
    进阶：如果给定的数组中含有负数，则会导致出现无限长度的排列。
    因此如果允许负数出现，则必须限制排列的最大长度，避免出现无限长度的排列，才能计算排列数。
    '''


if __name__ == '__main__':
    s = Solution()
    ret = s.combinationSum4([9], 3)
    print(ret)





