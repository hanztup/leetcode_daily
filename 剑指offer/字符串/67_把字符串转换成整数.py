# coding:utf-8

'''
date: 2021/6/1
content:
写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。

当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。

注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0。

说明：
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为[−231, 231− 1]。
如果数值超过这个范围，请返回 INT_MAX (231− 1) 或INT_MIN (−231) 。

示例1:
输入: "42"
输出: 42

示例2:
输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

示例3:
输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。

示例4:
输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。

示例5:
输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
    因此返回 INT_MIN (−231) 。

注意：本题与主站 8 题相同：https://leetcode-cn.com/problems/string-to-integer-atoi/
'''

class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """

        '''
        解法一
        思路：朴素做法，
             1. 判断特殊情况：字符串为空、字符串全为空格、字符串第一个非空字符不是"+-0123456789"
             2. 从下一位开始，判断正负号
             3. 注意三种退出条件：重复出现正负号、先出现数字再出现正负号、出现非整数字符（不在"0123456789"）
             4. 最后判断数字是否大于MAX_INT和MIN_INT
        时间复杂度：O(N)
        空间复杂度：O(1)
        '''
        # 空字符串
        if len(str) == 0:
            return 0
        # 字符串全为空格或字符串第一个非空字符不是数字
        valid = "0123456789"
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i == len(str):
            return 0
        if str[i] not in valid and str[i] not in '+-':
            return 0

        # 计数
        MAX_INT, MIN_INT = 2**31-1, -2**31
        flag = -1 if str[i] == '-' else 1
        res = 0
        while i < len(str):
            if (i-1 >= 0) and (str[i] in '+-') and (str[i-1] in '+-0123456789'):
                break

            if str[i] in '+-':
                i += 1
                continue

            if str[i] not in valid:
                break

            res = res * 10 + int(str[i])
            if res * flag <= MIN_INT:
                return MIN_INT
            if res * flag >= MAX_INT:
                return MAX_INT
            i += 1
        return res * flag


if __name__ == '__main__':
    s = Solution()
    ret = s.strToInt('  -91283472332 ')
    print(ret)










