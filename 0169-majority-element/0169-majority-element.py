class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
           d[i] = d.get(i,0)+1
        need = len(nums)//2
        for key,val in d.items(): 
            if val > need :
                return key
        