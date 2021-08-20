# coding:utf-8

'''
date: 2021/5/17
content:
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

示例1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

提示：

s.length <= 40000
注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        解法一
        思路：滑动窗口 + 窗口内确认重复下标
        时间复杂度：最坏O(n^2)
        空间复杂度：O(1)
        '''
        # if len(s) == 0 or len(s) == 1:
        #     return len(s)
        #
        # head, rear = 0, 0
        # res = 0
        #
        # while head < len(s):
        #     if head == rear:
        #         head += 1
        #         continue
        #
        #     tmp = rear
        #     while tmp < head:
        #         if s[tmp] != s[head]:
        #             tmp += 1
        #         else:
        #             rear = tmp + 1
        #             break
        #     res = max(res, head - rear + 1)
        #     head += 1
        # return res


        '''
        解法二
        思路：动态规划 + 哈希表
        时间复杂度: O(N)
        空间复杂度: O(1)
        '''

        visit = {}
        res, tmp = 0, 0

        for j in range(len(s)):
            i = visit.get(s[j], -1)
            visit[s[j]] = j
            tmp = tmp + 1 if tmp < j - i else j - i
            res = max(tmp, res)
        return res



