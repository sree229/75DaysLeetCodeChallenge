class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == [] or nums[0] >target or target >nums[-1]:
            return [-1,-1]
        l = 0
        h = len(nums)-1
        lis = []
        while l<h:
            mid = (l+h)//2
            if nums[mid] == target :
                h = mid
            elif nums[mid]< target :
                l = mid+1
            else :
                h = mid-1  
        if nums[l] == target :
            lis.append(l)
        else :
            lis.append(-1)
        l = 0
        h = len(nums)-1
        while l<h:
            mid = (l+h+1)//2
            if nums[mid] == target :
                l = mid
            elif nums[mid]< target :
                l = mid+1
            else :
                h = mid-1  
        if nums[l] == target :
            lis.append(l)
        else :
            lis.append(-1)
        return lis
      
