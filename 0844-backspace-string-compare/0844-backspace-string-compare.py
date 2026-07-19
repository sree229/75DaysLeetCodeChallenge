class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 =[]
        stack2 = []
        for i in s :
            if i!='#':
                stack1.append(i)
            else :
                if stack1 :
                    stack1.pop()
        s = ""
        while stack1 :
            s = stack1.pop() + s
        for i in t:
            if i!='#':
                stack2.append(i)
            else :
                if stack2 :
                    stack2.pop()
        t = ""
        while stack2 :
            t = stack2.pop() + t
        if s == t :
            return True
        return False

        
        