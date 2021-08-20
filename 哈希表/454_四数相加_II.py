# coding:utf-8

'''
date: 2021/5/25
content:

给定四个包含整数的数组列表A , B , C , D ,
计算有多少个元组 (i, j, k, l)，使得A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过231 - 1 。

例如:
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''


class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """

        '''
        解法一
        思路：先用visit字典存储nums1和nums2中的两数之和 a + b出现的次数，
             然后对于nums3和nums4中的两数之和c+d，找visit中0-(c+d)出现的次数即可
        时间复杂度:O(n^2)
        空间复杂度:O(n^2)
        '''

        visit = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                tmp_sum = nums1[i] + nums2[j]
                if tmp_sum not in visit:
                    visit[tmp_sum] = 1
                else:
                    visit[tmp_sum] += 1

        res = 0
        for k in range(len(nums3)):
            for l in range(len(nums4)):
                remain_sum = 0 - (nums3[k] + nums4[l])
                if remain_sum in visit:
                    res += visit[remain_sum]
        return res






















