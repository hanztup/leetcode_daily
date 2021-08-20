# coding:utf-8

'''
date: 2021/5/17
content:

在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:
s = "abaccdeff"
返回 "b"

s = ""
返回 " "

限制：
0 <= s 的长度 <= 50000
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        解法一
        思路：hash表
        时间复杂度：O(n)
        空间复杂度：O(1)
        '''
        if not s:
            return ' '

        visited = {}
        for i in range(len(s)):
            if s[i] not in visited:
                visited[s[i]] = 1
            else:
                visited[s[i]] += 1

        for j in range(len(s)):
            if visited[s[j]] == 1:
                return s[j]











