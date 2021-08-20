# coding:utf-8

'''
date: 2021/5/7
content:
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

限制：

0 <= matrix.length <= 100
0 <= matrix[i].length <= 100
注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/
'''

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or not matrix[0]:
            return []

        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []

        while True:
            # left -> right
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t += 1
            if t > b: break

            # top -> bottom
            for i in range(t, b+1):
                res.append(matrix[i][r])
            r -= 1
            if l > r: break

            # right -> left
            for i in range(r, l-1, -1):
                res.append(matrix[b][i])
            b -= 1
            if t > b: break

            # bottom -> top
            for i in range(b, t-1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r: break

        return res




# [[1,2,3],[4,5,6],[7,8,9]]
# [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
# [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]
# [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]


'''
相似题目：
https://leetcode-cn.com/problems/spiral-matrix-ii/

给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。


示例 1：

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：
1 <= n <= 20
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        '''
        解法一：四边界法
        '''
        if n == 0:
            return []

        matrix = [[None for _ in range(n)] for _ in range(n)]
        l, r, t, b = 0, n - 1, 0, n - 1
        num = 1

        while True:
            # left -> right
            for i in range(l, r+1):
                matrix[t][i] = num
                num += 1
            t += 1
            if t > b: break

            # top -> bottom
            for i in range(t, b+1):
                matrix[i][r] = num
                num += 1
            r -= 1
            if l > r: break

            # right -> left
            for i in range(r, l-1, -1):
                matrix[b][i] = num
                num += 1
            b -= 1
            if t > b: break

            # bottom -> top
            for i in range(b, t-1, -1):
                matrix[i][l] = num
                num += 1
            l += 1
            if l > r: break

        return matrix




