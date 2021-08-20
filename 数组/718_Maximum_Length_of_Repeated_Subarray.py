# coding:utf-8

'''
date: 2021/2/5
content:

给两个整数数组A和B，返回两个数组中公共的、长度最长的子数组的长度。

 

示例：

输入：
A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：
长度最长的公共子数组是 [3, 2, 1] 。
 

提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
'''

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """