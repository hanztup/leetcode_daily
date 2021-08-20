# coding:utf-8

'''
date: 2021/2/18
content:

给你一个正整数 n ，生成一个包含 1 到 n**2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

输入：n = 1
输出：[[1]]
'''


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        if n == 0:
            return []

        ret_array = []
        for i in range(n):
            ret_array.append([None] * n)
        # ret_array = [[None] * n] * n  # 创建二维数组

        loop = n // 2                 # 循环的圈数
        mid = n // 2                  # 中心坐标(n为奇数时用)
        startx, starty = 0, 0         # 起始坐标
        offset = 1                    # 偏移量，用于控制循环步数
        count = 1                     # 累加项


        while loop > 0:
            # i, j = startx, starty

            # 左 -> 右
            for j in range(starty, starty + n - offset):
                ret_array[startx][j] = count
                count += 1
            j += 1

            # 上 -> 下
            for i in range(startx, startx + n - offset):
                ret_array[i][j] = count
                count += 1
            i += 1


            # 右 -> 左
            while j > starty:
                ret_array[i][j] = count
                count += 1
                j -= 1

            # 下 -> 上
            while i > startx:
                ret_array[i][j] = count
                count += 1
                i -= 1


            startx += 1
            starty += 1
            offset += 2
            loop -= 1


        if n % 2 != 0:
            ret_array[mid][mid] = count

        return ret_array

if __name__ == '__main__':
    s = Solution()

    print(s.generateMatrix(4))


'''
1. 首先确定外层循环次数，即有几个圈
2. 其次确定内层循环，即四个方向，要注意选定一种标准（左闭右开或左开右闭）
'''
