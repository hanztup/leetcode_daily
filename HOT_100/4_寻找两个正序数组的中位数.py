# coding:utf-8

'''
date: 2021/7/28
content:
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。


示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000

示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000

示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
'''


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        '''
        解法一
        -思路：
          * 二分法，由于时间复杂度要求为O(logn)，表示这道题需要使用二分法来完成。难点在于：如何二分？
          * 参考了答案的思路:https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-s-114/
          * 将题目转换为"求两个有序数组的第k小的数"，大体思路上，每次比较A[k//2-1]和B[k//2-1]，可以排除大约k/2的数
          * 实现上有两点需要注意：
                * 实现思路为：
                    * （1）确定k
                    * （2）比较A[k//2-1]和B[k//2-1]
                    * （3）更新下一次k，转回步骤（2）
                    * 因此使用了递归
                * 遇到[k//2 - 1]大于某个数组的长度时，需要注意此时排除的数量并非k//2，而应该按照实际排除的数量来更新k（对应line 93）
        -时间复杂度: O(logn)
        -空间复杂度: O(n)，这里的实现还不太完善，因为每次在更新列表的时候会重新开辟内存，因此开辟内存空间的次数和比较的次数一致
        '''

        def find_smallest_k(A, B, k):
            if (not A) and (not B):
                # A和B均为空
                return 0

            if not A:
                # 仅A为空
                return B[k-1]

            if not B:
                # 仅B为空
                return A[k-1]

            if k == 1:
                return min(A[k-1], B[k-1])

            com_index = k // 2 - 1
            if com_index >= min(len(A), len(B)):
                com_index = min(len(A), len(B)) - 1

            if A[com_index] <= B[com_index]:
                A = A[com_index+1:]
            else:
                B = B[com_index+1:]
            return find_smallest_k(A, B, k - com_index - 1)  # 更新k：需要按照实际减少的数量，而非k//2

        total_len = len(nums1) + len(nums2)

        if total_len % 2 == 0:
            k1 = find_smallest_k(nums1, nums2, total_len // 2 + 1)
            k2 = find_smallest_k(nums1, nums2, total_len // 2)
        else:
            k1 = find_smallest_k(nums1, nums2, total_len // 2 + 1)
            k2 = k1

        return float(k1 + k2) / 2


if __name__ == '__main__':
    s = Solution()
    ret = s.findMedianSortedArrays(nums1=[], nums2=[3])
    print(ret)





