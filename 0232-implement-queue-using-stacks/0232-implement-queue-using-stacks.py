class MyQueue:
        
    def __init__(self):
        self.stack1 = [0]*100
        self.stack2 = [0]*100
        self.top1 =-1
        self.top2=-1
    
    def push(self, x: int) -> None:
        self.top1+=1
        self.stack1[self.top1]=x        

    def pop(self) -> int:
        while self.top1!=-1:
            self.top2+=1
            self.stack2[self.top2] = self.stack1[self.top1]
            self.top1-=1
        val = self.stack2[self.top2]
        self.top2-=1
        while self.top2!=-1:
            self.top1+=1
            self.stack1[self.top1]= self.stack2[self.top2]
            self.top2-=1
        return val

    def peek(self) -> int:
        
        while self.top1!=-1:
            self.top2+=1
            self.stack2[self.top2] = self.stack1[self.top1]
            self.top1-=1
        val =  self.stack2[self.top2]
        while self.top2!=-1:
            self.top1+=1
            self.stack1[self.top1]= self.stack2[self.top2]
            self.top2-=1
        return val        

    def empty(self) -> bool:
        return True if self.top1 == -1 else False



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()