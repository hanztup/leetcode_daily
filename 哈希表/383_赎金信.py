# coding:utf-8

'''
date: 2021/5/26
content:
给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，
判断第一个字符串 ransom 能不能由第二个字符串 magazines 里面的字符构成。
如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。
杂志字符串中的每个字符只能在赎金信字符串中使用一次。)

示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false

示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false

示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true

提示：
你可以假设两个字符串均只含有小写字母。
'''

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        '''
        解法一
        思路：使用哈希表visit存magazine中字母的出现次数，每次ransomNote出现一个字符，则visit中该字符次数减一
        时间复杂度：O(n)
        空间复杂度：O(1) （只有26个字母）
        '''
        visit = {}
        for i in range(len(magazine)):
            if magazine[i] not in visit:
                visit[magazine[i]] = 1
            else:
                visit[magazine[i]] += 1

        for j in range(len(ransomNote)):
            if ransomNote[j] not in visit or visit[ransomNote[j]] <= 0:
                return False
            else:
                visit[ransomNote[j]] -= 1
        return True




















