class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ","")
        operator = {"+": 1,"-": 1,"*": 2,"/": 2 }
        prefix = ""
        stack = []
        for i in s:
            if i.isdigit() :
                prefix +=i
            else :
                prefix+=","
                while stack and  operator[i] <= operator[stack[-1]] :
                    prefix+=stack.pop()
                    prefix += ","
                stack.append(i)
        prefix += ","       
        while stack :
            prefix+= stack.pop()  
            prefix +=","  
        stack1 = []
        for i in prefix.split(","):
            if not i :
                continue
            elif i.isdigit():
                stack1.append(int(i))
            else :
                a = stack1.pop()
                b = stack1.pop()
                if i == "+" :
                    stack1.append(a+b)
                elif i == "-" :
                    stack1.append(b-a) 
                elif i == "*" :
                    stack1.append(a*b)  
                elif i == "/" :
                    stack1.append(int(b/a))
                else :
                    pass
        return stack1[-1]
                