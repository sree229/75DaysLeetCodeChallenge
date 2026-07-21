class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in s:
            if not stack or i == "(" :
                stack.append(i)
            else:
                count = 0
                element = stack.pop()
                if element == "(" :
                    stack.append(str(1))
                    continue
                while element.isdigit():
                    count+=int(element)
                    element = stack.pop()
                stack.append(str(count*2))
        count = 0
        while stack :
            a = stack.pop()
            if a.isdigit():
                count+= int(a)
        return count
        