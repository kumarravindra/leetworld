'''
https://leetcode.com/problems/valid-palindrome/
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
"https://www.tutorialspoint.com/python3/string_isalnum.htm"
def is_Valid_Palindrome(str):
    left = 0
    right = len(str) - 1
    while left < right:
        while left < right and not str[left].isalnum():
            left += 1
        while left < right and not str[right].isalnum():
            right -= 1
        if left < right and str[left].lower() != str[right].lower():
            return False
        left += 1
        right -= 1
    return True

String_Test = "A man, a plan, a canal: Panama"
s = "race a car"
print(is_Valid_Palindrome(String_Test))
print(is_Valid_Palindrome(s))