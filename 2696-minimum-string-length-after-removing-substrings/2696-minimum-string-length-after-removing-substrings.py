class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for i in s :
            if not stack :
                stack.append(i)
                continue
            while stack and  (i == 'B' and stack[-1] == 'A') or (i=='D' and stack[-1]=='C'):
                stack.pop()
                break
            else :
                stack.append(i)
        return len(stack)
            
        