# coding:utf-8

'''
date: 2021/7/6
content:

给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加'+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

示例 2：
输入：nums = [1], target = 1
输出：1

提示：
1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
'''


class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''
        解法一
        思路： 动态规划，一维dp数组
        (1) 确定dp数组：dp[j]表示背包容量为j时的不同表达式的数目
        (2) 确定递推公式：dp[j] += dp[j-nums[i]]
        (3) 确定初始化：dp[0] = 1 (注意明白为什么不能等于0)，dp[1:] = 0
        (4) 遍历顺序：外层循环nums，内层倒序循环背包
        (5) 举例：略
        时间复杂度：
        空间复杂度：
        '''
        # 确定背包容量
        if (sum(nums) + target) % 2 != 0:
            return 0
        max_vol = (sum(nums) + target) // 2
        # 确定dp数组及初始化
        dp = [0] * (max_vol + 1)
        dp[0] = 1

        # 确定递推
        for i in range(len(nums)):
            for j in range(max_vol, nums[i] - 1, -1):
                dp[j] += dp[j-nums[i]]
        print(dp)
        return dp[max_vol]


if __name__ == '__main__':
    s = Solution()
    ret = s.findTargetSumWays([1, 1, 1, 1, 1], 3)
    print(ret)
