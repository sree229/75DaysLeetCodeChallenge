class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return nums[-1]
        arr = [nums[0],nums[1]] if nums[1]>nums[0] else [nums[0],nums[0]]
        for i in range(2,len(nums)):
                if  arr[-1] < arr[i-2]+nums[i] :
                    arr.append(arr[i-2]+nums[i])
                else :
                    arr.append(arr[-1])
        return arr[-1]
        