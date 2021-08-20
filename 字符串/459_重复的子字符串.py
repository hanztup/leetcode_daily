# coding:utf-8

'''
date: 2021/6/3
content:
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。
给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:
输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。

示例 2:
输入: "aba"
输出: False

示例 3:
输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
'''

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """

        '''
        解法一
        思路：借用KMP算法中构建next数组的方式，检查next数组最后一位的值是否等于字符串长度的一半.
             需要注意的是，在最后的判别边界上，我出了很多错，要吸取教训。
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

        next_table = get_next(s)
        # if next_table[-1] != 0 and len(s) % (len(s) - next_table[-1]) == 0:  # 逻辑是：当最长相等前后缀的长度不为0且能够被整个字符串长度除尽的时候，才能够实现重复
        #     return True
        # else:
        #     return False


        '''进一步，如果要求能够重复的最短的字符子串，尝试用以下方法'''
        if next_table[-1] != 0 and len(s) % (len(s) - next_table[-1]) == 0:
            ret_str = s[next_table[len(s)-1]:]
            return ret_str

        else:
            return False


if __name__ == '__main__':
    s = Solution()
    ret = s.repeatedSubstringPattern("abab")
    print(ret)
