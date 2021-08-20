# coding:utf-8

'''
date: 2021/7/19
content:
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，
判定s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。注意你可以重复使用字典中的单词。

示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        '''
        解法一
        思路：动态规划，完全背包，一维dp。要注意遍历的顺序
        时间复杂度：
        空间复杂度：
        '''

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for j in range(len(s) + 1):
            for i in range(len(wordDict)):
                if j >= len(wordDict[i]) and s[j-len(wordDict[i]): j] == wordDict[i]:
                    dp[j] = dp[j] or dp[j-len(wordDict[i])]

        return dp[len(s)] == 1


if __name__ == '__main__':
    s = Solution()
    sr = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","b"]
    ret = s.wordBreak(sr, wordDict)
    print(ret)
