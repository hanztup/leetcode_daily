# coding:utf-8

'''
date: 2021/7/28
content:

你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都 围成 一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统， 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下 ，能够偷窃到的最高金额。
示例 1:
输入:nums = [2,3,2]
输出:3
解释:你不能先偷窃 1 号房屋(金额 = 2)，然后偷窃 3 号房屋(金额 = 2), 因为他们是相邻的。

示例 2:
输入:nums = [1,2,3,1]
输出:4
解释:你可以先偷窃 1 号房屋(金额 = 1)，然后偷窃 3 号房屋(金额 = 3)。偷窃到的最高金额 = 1 + 3=4。

示例 3:
输入:nums = [0]
输出:0

提示:
1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，
        （1）确定dp数组。dp[j]表示经过第j个房屋，能够打劫的最高金额
        （2）确定递推公式:
             a. 把nums分成nums[:len-1]和nums[1:]两部分
             b. 分别对两部分使用递推：dp[j] = max(dp[j-1], dp[j-2] + nums[j])
             c. 将两部分得到的最大值进行max比较，取二者中最大的
        （3）确定初始化。dp[0] = nums[0], dp[1] = max(nums[0], nums[1])
        （4）确定遍历顺序。正序遍历
        （5）举例。
        时间复杂度：O(n), n为数组长度
        空间复杂度：O(n)，n为数组长度
        '''

        def rob_dp(refine_nums):
            dp = [0] * len(refine_nums)
            dp[0] = refine_nums[0]
            dp[1] = max(refine_nums[0], refine_nums[1])

            for j in range(2, len(refine_nums)):
                dp[j] = max(dp[j-1], dp[j-2] + refine_nums[j])
            return dp[len(refine_nums) - 1]

        length = len(nums)
        if length == 1:
            return nums[0]

        if length == 2:
            return max(nums)

        val1 = rob_dp(nums[:length-1])
        val2 = rob_dp(nums[1: length])

        return max(val1, val2)


if __name__ == '__main__':
    s = Solution()
    ret = s.rob([0])
    print(ret)

