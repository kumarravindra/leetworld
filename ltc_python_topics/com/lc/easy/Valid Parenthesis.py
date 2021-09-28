
def isValidParenthesis(str):
    dict = {"]":"[", "}":"{", ")":"("}
    stack = []

    for char in str:
        if char in dict.values():
            stack.append(char)
        elif char in dict.keys():
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []


str = "()"
print(isValidParenthesis(str))