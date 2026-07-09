class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxi  = 0
        i = 0
        j = len(nums)-1
        while i!=j :
            mid = (i+j)//2
            if nums[mid] < nums[mid+1] :
                i = mid+1
            else :
                j = mid
        print(i,j)
        if i==j:
            return i
           
            
        # while i<=j :
        #     if nums[i]>nums[j] :
        #         val = i
        #     else :
        #         val = j
        #     if nums[maxi] < nums[val]:
        #         maxi = val
        #     i+=1
        #     j-=1
        # return maxi 

