# coding:utf-8

'''
date: 2021/6/13
content:
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1

提示：
m ==obstacleGrid.length
n ==obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        '''
        解法一
        思路：动态规划
        （1）确定dp数列： dp[i][j] 表示走到第i行第j列时，所有的路径数
        （2）确定递推公式： dp[i][j] = dp[i--1][j] + dp[i][j-1]        if s[i-1][j] != 1 and s[i][j-1] != 1
                                  = dp[i-1][j]                      if s[i][j-1] == 1
                                  = dp[i][j-1]                      if s[i-1][j] == 1 
                                  = 0                               if s[i][j-1] == 1 and s[i-1][j] == 1 or s[i][j] == 1
        （3）初始化： dp[0, j] =  1 if s[0][j] != 1 elsle 0
                               dp[i, 0] = 1 if s[i][0] != 1 else 0
        （4）遍历顺序：按照行列两层for循环
        （5）举例：
        
                1	1	1
                1	0	1
                1	1	2
                
                
                1	0
                1	1

        时间复杂度：O(m*n)
        空间复杂度：O(m*n)
        '''
        # if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
        #     return 0
        #
        # m, n = len(obstacleGrid), len(obstacleGrid[0]),
        # dp = [[1 if obstacleGrid[i][j] == 0 else 0 for j in range(n)] for i in range(m)]
        # for j in range(1, n):
        #     if dp[0][j-1] == 0:
        #         dp[0][j] = 0
        # for i in range(1, m):
        #     if dp[i-1][0] == 0:
        #         dp[i][0] = 0
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if obstacleGrid[i][j] == 1:
        #             dp[i][j] = 0
        #         elif obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 1:
        #             dp[i][j] = 0
        #         elif obstacleGrid[i-1][j] == 1 and obstacleGrid[i][j-1] == 0:
        #             dp[i][j] = dp[i][j-1]
        #         elif obstacleGrid[i-1][j] == 0 and obstacleGrid[i][j-1] == 1:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] + dp[i][j-1]
        #
        # return dp[m-1][n-1]

        '''这道题可以写的更简洁，优化下写法'''
        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0:
            return 0

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 构建dp数组
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break

        for j in range(n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = 1
            else:
                break

        # 递推
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i-1][j] + dp[i][j-1]


        return dp[m-1][n-1]




if __name__ == '__main__':
    s = Solution()
    ret = s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    print(ret)



