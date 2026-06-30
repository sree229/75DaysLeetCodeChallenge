class Solution:
    def square(self,nn):
            squ = 0
            while nn > 0 :
                rem = nn%10
                squ += rem*rem
                nn = nn//10 
            return squ
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while  True:
            slow = self.square(slow)
            fast = self.square(self.square(fast))
            if slow==fast:
                break
        print(slow)
        return slow==1
       

