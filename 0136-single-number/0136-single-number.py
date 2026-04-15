class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dicti = {}
        for i in nums:
            dicti[i] = dicti.get(i,0)+1
        for key in dicti :
            if dicti[key] == 1:
                return key
        return 
        