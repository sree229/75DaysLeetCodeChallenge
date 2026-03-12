class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val ={}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in val :
                return val[d],i
            else :
                val[nums[i]] = i
        return -1
        
        
        
        