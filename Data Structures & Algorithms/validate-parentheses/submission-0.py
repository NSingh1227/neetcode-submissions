class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_dict = {"(" : ")", "{" : "}", "[": "]"}
        stack = []
        for char in s:
            if char in parenthesis_dict:
                stack.append(char)
            elif char in parenthesis_dict.values():
                if not stack:
                    return False
                if char == parenthesis_dict[stack[-1]]:
                    stack.pop()
                else:
                    return False
                    
        if stack:
            return False
        else:
            return True