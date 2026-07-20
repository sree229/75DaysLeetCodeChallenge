class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s :
                flag = 0
                while  stack and i == stack[-1] :
                    stack.pop()
                    flag = 1
                if not flag : 
                    stack.append(i)
        return "".join(stack)
        