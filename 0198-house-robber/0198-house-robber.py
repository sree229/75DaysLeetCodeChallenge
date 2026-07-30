class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [nums[0]]
        for i in range(1,len(nums)):
            if i>1 :
                if  arr[-1] < arr[i-2]+nums[i] :
                    arr.append(arr[i-2]+nums[i])
                else :
                    arr.append(arr[-1])
                
            else :
                if nums[i]>arr[-1]:
                    arr.append(nums[i])
                else :
                    arr.append(arr[-1])
        return arr[-1]
        