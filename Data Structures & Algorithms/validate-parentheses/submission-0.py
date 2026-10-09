class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for char in s:
            if char in "([{":
                stack.append(char)
            elif stack and stack[-1] == pairs[char]:
                stack.pop()
            else: 
                return False
        if not stack:
            return True
        else:
            return False