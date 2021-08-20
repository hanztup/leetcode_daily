# coding:utf-8

'''
date: 2021/6/11
content:
给你一个字符串s，「k 倍重复项删除操作」将会从 s中选择k个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。
你需要对s重复进行无限次这样的删除操作，直到无法继续为止。
在执行完所有删除操作后，返回最终得到的字符串。
本题答案保证唯一。


示例 1：
输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。

示例 2：
输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释：
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"

示例 3：
输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"

提示：

1 <= s.length <= 10^5
2 <= k <= 10^4
s中只含有小写英文字母。
'''

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        '''
        解法一
        思路：（超时）用两个栈stack1和stack2，每次遇到和栈顶相同的元素就不停地入栈stack2，直到确认是否满足k个，
              如果不满足再从stack2弹出回到stack1.
        时间复杂度：O(nk) 
        空间复杂度：O(n)
        '''
        # stack1 = []
        # stack2 = []
        #
        # for i in range(len(s)):
        #     if not stack1 or s[i] != stack1[-1]:
        #         stack1.append(s[i])
        #         continue
        #
        #     while stack1 and k > 1:
        #         if stack1[-1] == s[i]:
        #             stack2.append(stack1.pop())
        #         else:
        #             break
        #
        #     if len(stack2) == k - 1:
        #         stack2 = []
        #     else:
        #         while stack2:
        #             stack1.append(stack2.pop())
        #         stack1.append(s[i])
        #
        # return ''.join(stack1)

        '''
        解法二
        思路：上面解法一的问题在于，每次遇到和栈顶相同的元素，就不停地往回遍历确认。如果我们每次存元素到栈的时候，都用加上这个元            素当前出现的次数，那么就可以避免每次都往回遍历（只有满足次数为k时才弹出）：
             1. 使用栈
             2. 每次存（s[i], times）
        时间复杂度：
        空间复杂度：
        '''
        stack = []

        for i in range(len(s)):
            print(stack)
            if not stack or s[i] != stack[-1][0]:
                stack.append((s[i], 1))
                continue

            # s[i] == stack[-1][0]
            if stack[-1][1] == (k-1):
                # 依次弹出
                tmp = k
                while tmp > 1:
                    stack.pop()
                    tmp -= 1
            else:
                stack.append((s[i], stack[-1][1] + 1))

        str_list = [s for s, c in stack]
        return ''.join(str_list)


if __name__ == '__main__':
    s = Solution()
    ret = s.removeDuplicates(s="pbbcggttciiippooaais", k=2)
    print(ret)


