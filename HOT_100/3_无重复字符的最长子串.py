# coding:utf-8

'''
date: 2021/7/21
content:
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

示例1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0


提示：
0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成
'''


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        解法一
        思路：双指针
        时间复杂度：O(n ^ 2)
        空间复杂度：O(n)
        '''

        # fast, slow = 0, 0
        # max_sub_length = 0
        # sub_length = 0
        # visit = {}
        # while slow < len(s):
        #
        #     if fast < len(s) and s[fast] not in visit:
        #         visit[s[fast]] = 1
        #         sub_length += 1
        #         fast += 1
        #     else:
        #         if sub_length > max_sub_length:
        #             max_sub_length = sub_length
        #         sub_length = 0
        #         visit = {}
        #         slow += 1
        #         fast = slow
        #
        # return max_sub_length

        '''
        解法二
        思路：双指针优化
        时间复杂度：O(n ^ 2)
        空间复杂度：O(1)
        '''
        # slow, fast = 0, 0
        # max_sub_length = 0
        # while slow < len(s) and fast < len(s):
        #     tmp = slow
        #     while tmp < fast and s[tmp] != s[fast]:
        #         tmp += 1
        #
        #     if tmp == fast:  # 区间没有重复
        #         fast += 1
        #     else:
        #         if max_sub_length < (fast - slow):
        #             max_sub_length = fast - slow
        #         slow = tmp + 1
        #
        # max_sub_length = fast - slow if (fast - slow) > max_sub_length else max_sub_length
        # return max_sub_length

        '''
        解法三
        思路：滑动窗口，寻找每个字符开头的子串长度，然后记录最大长度
        时间复杂度：
        空间复杂度：
        '''

        right = -1
        visit = set()
        n = len(s)
        max_length = 0
        for i in range(n):
            if i != 0:
                visit.remove(s[i-1])
            while right + 1 < n and s[right+1] not in visit:
                visit.add(s[right+1])
                right += 1

            max_length = max(max_length, right - i + 1)
        return max_length


if __name__ == '__main__':
    s = Solution()
    ret = s.lengthOfLongestSubstring("pwwkew")
    print(ret)






