class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in d:
                if stack and stack.pop() == d[char]:
                    pass
                else:
                    return False
            else:
                stack.append(char)
        
        if stack:
            return False
        return True