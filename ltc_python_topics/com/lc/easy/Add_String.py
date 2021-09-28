'''
https://leetcode.com/problems/add-strings/
ord function : https://www.geeksforgeeks.org/ord-function-python/
'''

def add_String(str1, str2):
    numlist1 = list(str1)
    numlist2 = list(str2)
    carry = 0
    res = []

    while len(numlist1) > 0 or len(numlist2) > 0:
        n1 = ord(numlist1.pop()) - ord('0') if len(numlist1) > 0 else 0
        n2 = ord(numlist2.pop()) - ord('0') if len(numlist2) > 0 else 0

        temp = n1 + n2 + carry
        res.append(temp % 10)
        carry = temp // 10

    if carry: res.append(carry)
    return ''.join([str(i) for i in res])[::-1]

word1 = "540"
word2 = "290"
print(add_String(word1,word2))