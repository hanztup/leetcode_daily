# coding:utf-8

'''
date: 2021/6/16
content:
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

示例 2：
输入：nums = [1], k = 1
输出：[1]

示例 3：
输入：nums = [1,-1], k = 1
输出：[1,-1]

示例 4：
输入：nums = [9,11], k = 2
输出：[11]

示例 5：
输入：nums = [4,-2], k = 2
输出：[4]

提示：
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
'''


class my_queue(object):
    def __init__(self):
        self.queue = []
        self.length = 0

    def pop(self):
        if self.length != 0:
            return self.queue.pop()
        else:
            return -1

    def push(self, x):    
        if self.length != 0:
            rear_val = self.queue.pop()
            if x < rear_val:
                self.queue.append(rear_val)
                self.queue.append(x)
                self.length += 1
            else:
                self.queue.append(x)
        else:
            self.queue.append(x)
            self.length += 1

    def top(self):
        if self.length != 0:
            return self.queue[0]
        else:
            return -1


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


        '''
        解法一
        思路：单调队列
        时间复杂度：O(n)
        空间复杂度：O(k)
        '''
        ret = []
        count = 0
        queue = my_queue()
        for i in range(len(nums)):
            count += 1
            queue.push(nums[i])
            if count != k:
                continue
            max_val = queue.top()
            ret.append(max_val)
            count = 0
        return ret







