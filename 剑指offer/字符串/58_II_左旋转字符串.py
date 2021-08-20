# coding:utf-8

'''
date: 2021/6/1
content:
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

示例 1：
输入: s = "abcdefg", k = 2
输出:"cdefgab"

示例 2：
输入: s = "lrloseumgh", k = 6
输出:"umghlrlose"

限制：
1 <= k < s.length <= 10000
'''

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """

        '''
        解法一
        思路：先添加n+1到length-1的字符，再处理0到n的字符，这里用数组+join、或直接用字符串相加的方式都可以
        时间复杂度：O(N)
        空间复杂度：O(N) （用数组和字符串时所代表的含义不同，字符相加时每次都会新建一个内存存放新字符）
        '''
        # head, rear = n, 0
        # res = []
        # while head < len(s):
        #     res.append(s[head])
        #     head += 1
        # while rear < n:
        #     res.append(s[rear])
        #     rear += 1
        # return ''.join(res)

        # 上述写法可优化：
        # res = []
        # for i in range(len(s)):
        #     res.append(s[(i+n) % len(s)])  # 看评论提到：遇到 "到尾端就要从头开始" 的，基本都可以用取余
        # return ''.join(res)


        '''
        解法二
        思路：1. 先翻转0到n的部分
             2. 再翻转n+1到length-1的部分
             3. 最后翻转整个字符串
        时间复杂度：O(N)
        空间复杂度：O(N) (要先把字符串变为数组)
        '''
        # 转存为数组
        s_list = list(s)

        # 翻转函数
        def reverse_ij(l, i, j):
            while i < j:
                tmp = l[j]
                l[j] = l[i]
                l[i] = tmp
                i += 1
                j -= 1
            return

        reverse_ij(s_list, 0, n-1)              # 翻转0 ~ (n -1) 部分
        reverse_ij(s_list, n, len(s_list) - 1)  # 翻转n ~ (len(s) -1) 部分
        reverse_ij(s_list, 0, len(s_list) - 1)  # 翻转0 ~ (len(s) -1) 部分

        return ''.join(s_list)








