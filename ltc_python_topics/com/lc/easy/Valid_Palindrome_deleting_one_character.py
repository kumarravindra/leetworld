'''
https://leetcode.com/problems/valid-palindrome-ii/

    # Time: O(n)
    # Space: O(n)
'''

def validPalindrome(st):
    i = 0
    j = len(st) - 1

    while i < j:
        if st[i] != st[j]:
            delete_i = st[i:j]
            delete_j = st[i + 1:j + 1]
            print(delete_i[::-1])
            print(delete_j[::-1])
            return delete_i == delete_i[::-1] or delete_j == delete_j[::-1]
        i += 1
        j -= 1
    return True
strings = "abbca"
print(validPalindrome(strings))