# coding:utf-8

'''
date: 2021/7/9
content：
有N件物品和一个最多能背重量为W的背包。
第i件物品的重量是weight[i]，得到的价值是value[i] 。
每件 物品都有无限个(也就是可以放入背包多次)，求解将哪些物品装入背包里物品价值总和最大。

举例：
有3件物品，重量分别为：[1, 3, 4]，价值分别为：[15, 20, 30]
背包最大重量为4
背包所背最大价值为：60
'''

class Solution(object):
    def dp_bag(self, max_vol, weights, values):

        '''
        完全背包原理，计划采用二维dp及一维dp数组两种写法，同时要能够明确回答以下问题：
        （1）循环嵌套的顺序（反过来写是否可以？）
        （2）初始化的逻辑
        '''

        '''
        解法一
        思路：动态规划，一维dp数组
        时间复杂度：
        空间复杂度：
        '''
        # dp = [0] * (max_vol + 1)
        #
        # for i in range(len(weights)):
        #     for j in range(weights[i], max_vol+1):
        #         dp[j] = max(dp[j], dp[j-weights[i]] + values[i])
        # print(dp)
        # return dp[max_vol]


        '''
        解法二
        思路：动态规划，二维数组
        空间复杂度：
        时间复杂度：
        '''
        dp = [[0 for _ in range(max_vol+1)] for _ in range(len(weights))]
        for j in range(weights[0], max_vol+1):
            dp[0][j] = dp[0][j-weights[0]] + values[0]

        for i in range(1, len(weights)):
            for j in range(1, max_vol + 1):
                if j < weights[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i]] + values[i])

        print(dp)
        return dp[len(weights)-1][max_vol]




if __name__ == '__main__':
    s = Solution()
    ret = s.dp_bag(4, [1, 3, 4], [15, 20, 25])
    print(ret)
