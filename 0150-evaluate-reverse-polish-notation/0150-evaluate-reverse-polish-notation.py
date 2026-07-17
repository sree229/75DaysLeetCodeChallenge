class Solution:
    def fun(self,ch,stack) :
        a = stack.pop()
        b = stack.pop()
        match ch :
            case "+" :
             return (a+b)
            case "-" :
             return (b-a)
            case "*" :
                 return (a*b)
            case "/" : 
                return int(b/a)
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+","*","/","-"] :
               res =  self.fun(i,stack)
               stack.append(res)
            else :
                stack.append(int(i))
        return stack[-1]


















































        