class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        n = {}
        count = 0
        for i in nums :
            n[i] = n.get(i,0)+1
        for key in n:
            if n[key] == 2:
                count ^= key
        return count
        
