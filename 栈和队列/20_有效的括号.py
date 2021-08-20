# coding:utf-8

'''
date: 2021/6/10
content:
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例2：
输入：s = "()[]{}"
输出：true

示例3：
输入：s = "(]"
输出：false

示例4：
输入：s = "([)]"
输出：false

示例5：
输入：s = "{[]}"
输出：true
提示：
1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        解法一
        思路：保存一个栈stack：
             - 每次遇到一个左边括号"([{",就入栈
             - 每次遇到一个右边括号")]}",就和栈顶元素比较：
               （1）栈顶为空，则返回False，
               （2）和栈顶元素不匹配，则返回False
               （3）和栈顶元素匹配，则弹出栈顶元素
             - 最后判断栈是否为空，为空则返回True，反之为False
        时间复杂度：O(n)
        空间复杂度：O(n/2)
        '''
        if len(s) == 0:
            return True

        symbol_map = {')': '(',
                      ']': '[',
                      '}': '{'}
        stack = []
        for i in range(len(s)):
            if not stack:
                if s[i] not in symbol_map:
                    stack.append(s[i])
                else:
                    return False
            else:
                if s[i] not in symbol_map:
                    stack.append(s[i])
                else:
                    if stack[-1] == symbol_map[s[i]]:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0


if __name__ == '__main__':
    s = Solution()
    ret = s.isValid('(])')
    print(ret)