# coding:utf-8

'''
date: 2021/5/18
content:
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
'''


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        '''
        解法一
        思路：判断长度是否一致，再判断两者字母是否一致
        时间复杂度：O(n)
        空间复杂度：O(1), 所有字母只有26个
        '''

        if len(s) != len(t):
            return False

        visit = {}
        for i in range(len(s)):
            if s[i] not in visit:
                visit[s[i]] = 1
            else:
                visit[s[i]] += 1

        for j in range(len(t)):
            if t[j] not in visit:
                return False
            else:
                visit[t[j]] -= 1

        for k, v in visit.items():
            if v != 0:
                return False
        return True

