# coding:utf-8

'''
date: 2021/6/2
content:

实现strStr()函数。
给你两个字符串haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。
如果不存在，则返回 -1 。

说明：
当needle是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当needle是空字符串时我们应当返回 0 。这与 C 语言的strstr()以及 Java 的indexOf()定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1

示例 3：
输入：haystack = "", needle = ""
输出：0


提示：
0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''
        解法一
        思路：经典KMP算法
        时间复杂度：
        空间复杂度：
        '''

        def get_next(s):
            nxt = []
            nxt.append(0)
            x = 1
            front = 0

            while x < len(s):
                if s[x] == s[front]:
                    x += 1
                    front += 1
                    nxt.append(front)
                elif front:
                    front = nxt[front-1]
                else:
                    x += 1
                    nxt.append(0)
            return nxt

        def search(s, p, nxt):
            point_s = 0
            point_p = 0
            ret = []

            while point_s < len(s):
                if s[point_s] == p[point_p]:
                    point_s += 1
                    point_p += 1
                elif point_p:
                    point_p = nxt[point_p-1]
                else:
                    point_s += 1

                if point_p == len(p):
                    ret.append(point_s - len(p))
                    point_p = nxt[point_p-1]

            return ret

        if not needle:
            return 0

        next_table = get_next(needle)  # 这里我犯过错：计算了主串的前缀表。要注意这里是计算匹配串的前缀表
        print(next_table)
        res = search(haystack, needle, next_table)
        if res:
            return res[0]
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    result = s.strStr("mississippi", "issip")
    print(result)
