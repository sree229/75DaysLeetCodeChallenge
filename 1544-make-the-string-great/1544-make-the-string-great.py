class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s :
            if not stack :
                stack.append(i)
                continue
            val = ord(i)
            while stack and ((val+32 == ord(stack[-1])) or (val-32 == ord(stack[-1]))) :
                stack.pop()
                break 
            else :
                stack.append(i)
        return "".join(stack)