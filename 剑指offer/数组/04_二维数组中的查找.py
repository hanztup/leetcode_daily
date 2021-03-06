# coding:utf-8


'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

示例:
现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target=5，返回true。

给定target=20，返回false。

限制：

0 <= n <= 1000

0 <= m <= 1000

注意：本题与主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/
'''

class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) ==0:
            return False

        n = len(matrix)
        m = len(matrix[0])

        '''
        解法一：双层for循环
        时间复杂度: O(n * m)
        空间复杂度：O(1)
        '''
        # for row in range(n):
        #     for col in range(m):
        #         if matrix[row][col] == target:
        #             return True
        # return False


        '''
        解法二：根据二维矩阵右上角划到左下角的思路进行判断
        时间复杂度：O(m+n)
        空间复杂度：O(1)
        '''
        row, col = 0, m-1
        while row <= n-1 and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] == target:
                return True
            else:
                col -= 1

        return False






