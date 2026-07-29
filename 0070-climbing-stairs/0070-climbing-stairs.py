class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n ==1 :
        #     return 1
        # if n ==0 :
        #     return 1
        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        if n ==1 :
            return 1
        if n ==0 :
            return 1
        dic = {0:1,1:1}
        i = 2 
        while i<=n:
            dic[i] = dic[i-1]+dic[i-2]
            i+=1
        return dic[n]