# coding:utf-8

'''
date: 2021/2/3
content:
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
'''


class Solution(object):
    def moveZeroes1(self, nums):
        """
        前后指针 --> 这个方式在这道题下不行，因为会使得顺序改变了
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return nums

        length = len(nums)
        left, right = 0, length - 1

        while left <= right:
            if nums[right] == 0:
                right -= 1
            elif nums[left] == 0:
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp

                left += 1
                right -= 1
            else:
                left += 1
        return nums


    def moveZeroes2(self, nums):
        """
        快慢指针
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return

        slow = 0
        # method 1
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        # 将slow至末尾部分补充为0
        for i in range(slow, len(nums)):
            nums[i] = 0


        # method 2
        # for fast in range(len(nums)):
        #     if nums[fast] != 0:
        #         tmp = nums[slow]
        #         nums[slow] = nums[fast]
        #         nums[fast] = tmp
        #         slow += 1

        return nums





if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes1([0,1,0,3,12]))
    print(s.moveZeroes2([0,1,0,3,12]))
