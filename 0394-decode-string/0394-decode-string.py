class Solution:
    def decodeString(self, s: str) -> str:
        num = ""
        stack = []
        for i in s :
            if i.isdigit() :
                num += i
            elif i == "[" :
                stack.append(num)
                stack.append(i)
                num  = ""
            elif i.isalpha() :
                stack.append(i)
            else :
                st = ""
                while stack and stack[-1]!="[":
                    d = stack[-1]
                    if d.isalpha():
                        st = d+st
                    else :
                        st*=int(d)
                    stack.pop()
                if stack :
                    stack.pop()
                    st*=int(stack[-1])
                    stack.pop()
                stack.append(st)
        st = ""
        while stack :
            st =stack[-1] +st
            stack.pop()
        return st
        