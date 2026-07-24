class MinStack(object):

    def __init__(self):
        self.stack = []
        self.el = []

    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack.append(value)
        if not self.el :
            self.el.append(value)
        else :
           if value <= self.el[-1] :
                self.el.append(value)

    def pop(self):
        """
        :rtype: None
        """
        if self.el[-1] == self.stack[-1] :
            self.el.pop()
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.el :
            return  self.el[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()