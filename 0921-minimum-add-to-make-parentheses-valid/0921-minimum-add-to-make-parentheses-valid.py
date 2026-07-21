class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        match = { "(" :")", "[":"]","{":"}" }
        for i in s:
            if stack and  i == match.get(stack[-1],"random"):
                stack.pop()
            else :
                stack.append(i) 
        return len(stack)
