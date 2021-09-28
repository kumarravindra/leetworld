"""
https://leetcode.com/problems/reverse-integer/
https://leetcode.com/problems/reverse-integer/submissions/
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).



Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""

def reverse_integer(num):
    flag = False
    num_string = str(num)

    "if negative int remove the sign"
    if num_string[0] == '-':
        num_string = num_string[1:]
        flag = True

    "reverse the string"
    rev_str = num_string[::-1]

    "add the sign if remove before"
    if flag:
        rev_str = '-' + rev_str

    "if overflow return 0"
    rev_str = int(rev_str)
    if rev_str > 2**31 - 1 or rev_str < -2**31:
        rev_str = 0
    return rev_str

numbers = 123
print(reverse_integer(numbers))