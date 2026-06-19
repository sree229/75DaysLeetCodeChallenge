class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        ans = ""
        sp = 1
        if x<0 :
            x = abs(x)
            sp = -1
        while x!=0 :
            add = x%10
            x = x//10
            ans += str(add)
        ans = int(ans)*sp
        if ans < -2**31 or ans > 2**31-1:
             return 0
        return ans
            
        

