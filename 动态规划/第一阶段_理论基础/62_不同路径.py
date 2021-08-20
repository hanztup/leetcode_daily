# coding:utf-8

'''
date: 2021/6/12
content:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        '''
        解法一
        思路：二维动态规划
        （1）dp[i][j] 表示到第i行第j列的格子时，存在的路径数
        （2）确定递推公式： dp[i][j] = dp[i][j-1] + dp[i-1][j] 
        （3）初始化：dp[0, :] = 1; dp[:, 0] = 1
        （4）遍历的顺序：用两个for循环分别遍历行和列
        （5）举例实验:
            m=2, n=3
                1	1	1
                1	2	3
            m=3, n=7
                1	1	1	1	1	1	1
                1	2	3	4	5	6	7
                1	3	6	10	15	21	28
        时间复杂度：O(m*n)
        空间复杂度：O(m*n)
        '''
        # 构建二维dp数组，第一行和第一列均为1
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # 递推
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]


if __name__ == '__main__':
    s = Solution()
    ret = s.uniquePaths(3, 3)
    print(ret)
