class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s :
            d[i] = d.get(i,0)+1 
        lis = sorted(d.items(), key=lambda x: x[1], reverse=True)
        print(lis)
        res = ""
        for key,val in lis :
            res += key*val
        return res
        
        