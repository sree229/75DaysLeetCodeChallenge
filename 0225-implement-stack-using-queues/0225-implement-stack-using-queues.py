class MyStack:

    def __init__(self):
        self.queue1 = [0]*100
        self.queue2 = [0]*100
        self.front = -1
        self.rear = -1
        self.front1 = -1
        self.rear1 = -1
    def push(self, x: int) -> None:
        if self.empty() : 
            self.front = 0
            self.rear = 0
            self.queue1[self.rear] = x
        else :
            self.rear+=1
            self.queue1[self.rear]=x 

    def pop(self) -> int:
        while self.rear>=self.front :
            if self.front1==-1:
                self.front1= 0
                self.rear1 = 0
                self.queue2[self.rear1] = self.queue1[self.rear]
            else :
                self.rear1+=1
                self.queue2[self.rear1] = self.queue1[self.rear]
            self.rear-=1 
        val = self.queue2[self.front1]
        self.front1+=1
        while self.rear1>= self.front1 : 
            if self.empty() :
                self.front = 0
                self.rear = 0
                self.queue1[self.rear] = self.queue2[self.rear1]
            else :
                self.rear+=1
                self.queue1[self.rear] = self.queue2[self.rear1]
            self.rear1-=1
        return val

    def top(self) -> int: 
        if self.empty() :
            return 
        return self.queue1[self.rear] 
        
    def empty(self) -> bool:
        if  self.rear == -1 :
            return True
        else :
            return False




# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()