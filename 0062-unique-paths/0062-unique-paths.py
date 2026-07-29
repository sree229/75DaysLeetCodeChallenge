class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def fac(n):
            val = 1
            for i in range(2,n+1):
                val*=i
            return val
        down = fac(m-1)
        right = fac(n-1)
        top = fac(m+n-2)  
        res = top // (down*right)
        return res

