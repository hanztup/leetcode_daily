# coding:utf-8

'''
date: 2021/7/23
content:
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃 到的最高金额。

示例 1:
输入:[1,2,3,1]
输出:4
解释:偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
偷窃到的最高金额 = 1 + 3 = 4 。

示例 2:
输入:[2,7,9,3,1]
输出:12
解释:偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
偷窃到的最高金额 = 2 + 9 + 1 = 12 。 提示:
0 <= nums.length <= 100 0 <= nums[i] <= 400
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，01背包，一维dp
        时间复杂度：
        空间复杂度：
        '''
        # dp = [0] * len(nums)
        # max_val = 0
        #
        # for i in range(0, len(nums)):
        #     for j in range(i-1):
        #         dp[i] = max(dp[i], dp[j])
        #     dp[i] += nums[i]
        #     max_val = max(max_val, dp[i])
        # return max_val


        '''
        解法二
        思路：动态规划思路优化
        时间复杂度：
        空间复杂度：
        '''

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        print(dp)
        return dp[len(nums) - 1]


if __name__ == "__main__":
    s = Solution()
    ret = s.rob([1, 1])
    print(ret)
