class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        steps = {1:1,2:2}
        i = 3
        while i<=n:
               a =  i-1
               b = i-2
               c = steps[a]+steps[b]
               steps[i] = c
               i+=1
        return c




        
        