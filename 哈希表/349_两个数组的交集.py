# coding:utf-8

'''
date: 2021/5/19
content:
给定两个数组，编写一个函数来计算它们的交集。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]


说明：

输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。

'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        '''
        解法一
        思路：（1）先遍历nums1，将nums1中的所有值用字典保存，key为值，value为False；
             （2）再遍历nums2，如果nums2中的值出现在visit中，则将value改为True
             （3）最后遍历visit（key，value），返回value is True的key即可
        时间复杂度：O(n)
        空间复杂度：O(n + m)
        '''
        if len(nums1) == 0 or len(nums2) == 0:
            return []

        visit = {}
        for i in range(len(nums1)):
            if nums1[i] not in visit:
                visit[nums1[i]] = False # 不管在nums1中出现了多少次，都令他的value为False

        for j in range(len(nums2)):
            if nums2[j] not in visit:
                continue
            visit[nums2[j]] = True

        res = []
        for k, v in visit.items():
            if v:
                res.append(k)
        return res

        '''
        解法二
        思路：排序 + 双指针; 
            （1）先对两个数组进行排序，使得每个数组中的数字从小到大排列 
            （2）设立两个指针index1、index2分别指向两个数组，当nums1[index1] == nums2[index2]判断返回数组中最后一位（res递增）是否和其相等，
                当nums1[index1] != nums2[index2]时，谁小谁的指针往后移一位，直到超出长度限制
        时间复杂度：O(mlogm + nlogn)  (排序用)
        空间复杂度：O(logm + logn)  （排序用）
        '''

        nums1.sort()
        nums2.sort()

        len1, len2 = len(nums1), len(nums2)
        res = []
        index1 = index2 = 0

        while index1 < len1 and index2 < len2:
            if nums1[index1] == nums2[index2]:
                if not res or nums1[index1] != res[-1]:
                    res.append(nums1[index1])
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                index2 += 1

        return res




