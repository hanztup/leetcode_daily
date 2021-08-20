# coding:utf-8

'''
date: 2021/6/29
content:
给你一个 只包含正整数 的 非空 数组nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。


示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        解法一
        思路：动态规划，转化为01背包问题
        时间复杂度：O(n ^ 2)
        空间复杂度：O(n)
        '''
        if len(nums) == 0:
            return True

        if sum(nums) % 2 != 0:
            return False

        max_vol = sum(nums) // 2
        weights = nums
        values = nums

        # 确定dp数组
        dp = [0] * (max_vol + 1)
        for i in range(len(weights)):
            for j in range(max_vol, weights[i]-1, -1):
                dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
        print(dp)

        if dp[max_vol] == max_vol:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    ret = s.canPartition([2, 2, 1, 1])
    print(ret)


