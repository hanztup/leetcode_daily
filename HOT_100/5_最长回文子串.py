# coding:utf-8

'''
date: 2021/11/22
content:

给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
示例 3：

输入：s = "a"
输出："a"
示例 4：

输入：s = "ac"
输出："a"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """


        '''
        解法一
        思路：动态规划
        时间复杂度：O(N^2)
        空间复杂度：O(N^2)
        '''

        if len(s) <= 1:
            return s

        max_len = 1
        begin = 0
        n = len(s)

        # 确定dp
        dp = [[False for _ in range(n)] for _ in range(n)]

        # 初始化
        for i in range(n):
            dp[i][i] = True

        # 先对子串长度循环，再对左边界循环
        for L in range(2, n+1):
            for i in range(n):  # 左边界

                j = L + i - 1  # 右边界
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin: begin+max_len]


if __name__ == '__main__':
    s = Solution()
    ret = s.longestPalindrome('efbaabcd')
    print(ret)
