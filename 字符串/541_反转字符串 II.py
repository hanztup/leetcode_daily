# coding:utf-8

'''
date: 2021/5/29
content:
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:
输入: s = "abcdefg", k = 2
输出: "bacdfeg"

提示：
该字符串只包含小写英文字母。
给定字符串的长度和 k 在 [1, 10000] 范围内。
'''

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        '''
        解法一
        思路：双层循环
        时间复杂度：O(n*k)
        空间复杂度：O(n)
        '''

        list_s = list(s)  # convert to string list
        for i in range(0, len(list_s), 2*k):
            if i + k <= len(list_s): # remain length > k
                head, rear = i, i + k - 1
            else:
                head, rear = i, len(list_s) - 1

            while head < rear:
                tmp = list_s[rear]
                list_s[rear] = list_s[head]
                list_s[head] = tmp

                head += 1
                rear -= 1

        return ''.join(list_s)



