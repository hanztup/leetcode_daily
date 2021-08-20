# coding:utf-8

'''
date: 2021/7/2
content:
有一堆石头，用整数数组stones表示。其中stones[i] 表示第 i 块石头的重量。

每一回合，从中选出任意两块石头，然后将它们一起粉碎。假设石头的重量分别为x 和y，且x <= y。那么粉碎的可能结果如下：

如果x == y，那么两块石头都会被完全粉碎；
如果x != y，那么重量为x的石头将会完全粉碎，而重量为y的石头新重量为y-x。
最后，最多只会剩下一块 石头。返回此石头 最小的可能重量 。如果没有石头剩下，就返回 0。

示例 1：
输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

示例 2：
输入：stones = [31,26,33,21,40]
输出：5

示例 3：
输入：stones = [1,2]
输出：1

提示：
1 <= stones.length <= 30
1 <= stones[i] <= 100
'''


class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        '''
        解法一
        思路：动态规划，一维dp数组
        时间复杂度：
        空间复杂度：
        '''
        total_vol = sum(stones)
        max_vol = total_vol // 2  # 注意下取整
        dp = [0] * (max_vol + 1)

        for i in range(len(stones)):
            for j in range(max_vol, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        remain_val = total_vol - dp[max_vol]

        return remain_val - dp[max_vol]


if __name__ == "__main__":
    s = Solution()
    ret = s.lastStoneWeightII([2,7,4,1,8,1])
    print(ret)






