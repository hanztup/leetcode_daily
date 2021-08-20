# coding:utf-8

'''
date: 2021/6/11
content:
给出由小写字母组成的字符串S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：

输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

提示：

1 <= S.length <= 20000
S 仅由小写英文字母组成。
'''


class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        解法一
        思路：使用栈来进行过滤，遍历字符串s，如果s[i]和栈顶元素不一样则入栈，反之则弹出栈顶元素
        时间复杂度：O(N)
        空间复杂度：O(N)
        '''

        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])

        return ''.join(stack)

