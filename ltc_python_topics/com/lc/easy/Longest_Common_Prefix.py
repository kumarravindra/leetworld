'''
https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

def longest_common_prefix(str):
    if not str:
        return ""
    short_word = min(str, key=len)

    for i, ch in enumerate(short_word):
        for otherwords in str:
            if otherwords[i] != ch:
                return short_word[:i]
    return short_word


strr = ["flower","flow","flight"]
print(longest_common_prefix(strr))