class Solution:
    def isValid(self, s: str) -> bool:
    
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch not in mapping:
                stack.append(ch)
            else:
                if not stack or stack.pop() != mapping[ch]:
                    return False

        return not stack