class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        ans = 0
        sp = 1
        if x<0 :
            x = abs(x)
            sp = -1
        while x!=0 :
            digit = x%10
            x =  x//10
            ans = ans*10+digit
        ans = ans*sp
        if ans < -2**31 or ans > 2**31-1:
             return 0
        return ans
            
        

