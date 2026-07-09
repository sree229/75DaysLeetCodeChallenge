class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxi  = 0
        i = 0
        j = len(nums)-1
        while i<=j :
            if nums[i]>nums[j] :
                val = i
            else :
                val = j
            if nums[maxi] < nums[val]:
                maxi = val
            i+=1
            j-=1
        return maxi