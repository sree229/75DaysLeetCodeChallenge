class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lis = []
        for i in range(len(nums)):
            if nums[i] == target :
                lis.append(i)
        if len(lis)>1 :
            return [lis[0],lis[-1]]
        elif len(lis)==1:
            return lis+lis
        else :
            return [-1,-1]
