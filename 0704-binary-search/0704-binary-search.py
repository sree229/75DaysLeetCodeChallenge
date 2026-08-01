class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def fun(left,right) :
            if left>right :
                return -1
            mid = (left+right)//2
            if nums[mid] == target :
                return mid 
            if nums[mid] <target:
                return fun(mid+1,right)
            if nums[mid]> target:
                return fun(left,mid-1) 
        left = 0
        right = len(nums)-1
        return fun(left,right)             