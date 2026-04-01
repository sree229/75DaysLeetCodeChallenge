class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [0]*len(tokens)
        top = -1
        for i in tokens :
            if i == "+" or i == "-" or i == "*" or i == "/" :
                a = stack[top]
                top-=1
                b = stack[top]
                if i == "+"  :
                    stack[top] = a+b
                elif i == "-" :
                    stack[top]= b-a
                elif  i == "*" :
                    stack[top]= a*b 
                else :
                    stack[top]= int(b/a)
            else :
                top+=1
                stack[top] = int(i)
        return stack[top]

        