'''
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
import collections


def find_First_Unique_Char_In_String(str):
    # build hash map : character and how often it appears

    count = collections.Counter(str)
    for i, char in enumerate(str):
        if count[char] == 1:
            return i

    return -1

strings = "leetcodel"
print(find_First_Unique_Char_In_String(strings))


