# coding:utf-8

'''
date: 2021/5/31
content:

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1：
输入：s = "We are happy."
输出："We%20are%20happy."

限制：
0 <= s 的长度 <= 10000
'''

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        解法一
        思路：用两个指针，一个指针step代表遍历的次数，一个指针i代表遍历的位置
        时间复杂度：O(N)
        空间复杂度：O(N^2)
        '''
        # replace = '%20'
        # last = len(s)
        # step, i = 0, 0
        #
        # while step < last:
        #     if s[i] == ' ':
        #         s = s[:i] + replace + s[i+1:]
        #         i += 3
        #     else:
        #         i += 1
        #     step += 1
        # return s

        '''
        解法二
        思路：使用额外的空间list，遍历字符串，每次遇到空格时，向list填充%20，最后再用join方法
        时间复杂度：O(N)
        空间复杂度: O(N)
        '''

        # res = []
        # for c in s:
        #     if c == ' ':
        #         res.append('%20')
        #     else:
        #         res.append(c)
        # return ''.join(res)
