# coding:utf-8

'''
date: 2021/5/31
content:
给你一个字符串 s ，逐个翻转字符串中的所有单词。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。

说明：
输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
翻转后单词间应当仅用一个空格分隔。
翻转后的字符串中不应包含额外的空格。

示例 1：
输入：s = "the sky is blue"
输出："blue is sky the"

示例 2：
输入：s = " hello world "
输出："world hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。

示例 3：
输入：s = "a good example"
输出："example good a"
解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。

示例 4：
输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"

示例 5：
输入：s = "Alice does not even like bob"
输出："bob like even not does Alice"

提示：
1 <= s.length <= 104
s 包含英文大小写字母、数字和空格 ' '
s 中 至少存在一个 单词

进阶：
请尝试使用O(1) 额外空间复杂度的原地解法。
'''

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        '''
        解法一
        思路：朴素做法，借用O(N)空间
        时间复杂度：O(N)
        空间复杂度：O(m) m为单词个数
        '''
        # # 先保存所有的单词
        # words = []
        # word = ""
        # for i in range(len(s)):
        #     if s[i] == ' ':
        #         if word:
        #             words.append(word)
        #             word = ""
        #     else:
        #         word += s[i]
        # if word: words.append(word)
        #
        # # 翻转单词列表
        # i, j = 0, len(words) - 1
        # while i <= j:
        #     tmp = words[j]
        #     words[j] = words[i]
        #     words[i] = tmp
        #     i += 1
        #     j -= 1
        #
        # res = ' '.join(words)
        # return res

        '''
        解法二
        思路：原地修改，尽管因为python中string不可修改，这样操作要花费额外的空间，但还是应该锻炼这样的思路
             1. 先去除两端、中间的多余空格（可考虑多种方法，例如融合"数组删除某个元素"中的方法）
             2. 将整个字符串进行翻转
             3. 将每个单词进行翻转
        时间复杂度：O(N)
        空间复杂度：O(N)
        '''
        def clean_space(s):
            left, right = 0, len(s) - 1
            ret_list = []
            # 去除左边多余的空格
            while (left < right) and (s[left] == ' '):
                left += 1

            # 去除右边多余的空格
            while (left < right) and (s[right] == ' '):
                right -= 1

            # 去除中间多余的空格
            for i in range(left, right+1):
                if i > 0 and s[i] == ' ' and s[i-1] == ' ':
                    continue
                ret_list.append(s[i])
            return ret_list

        def reverse_list(l, i, j):
            while i < j:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
            return

        def reverse_each_word(l):
            start, end = 0, 0
            while start < len(l):
                while (end < len(l)) and (l[end] != ' '):
                    end += 1
                    continue

                reverse_list(l, start, end-1)  # 翻转start ~ (end-1部分)
                end += 1
                start = end
            return

        s_list = clean_space(s)                   # 清洗两端及中间多余空格
        reverse_list(s_list, 0, len(s_list) - 1)  # 将整个字符串进行翻转
        reverse_each_word(s_list)                 # 将字符串中每个单词翻转
        return ''.join(s_list)


if __name__ == '__main__':
    s = Solution()
    ret = s.reverseWords(" ")
    print(ret)




