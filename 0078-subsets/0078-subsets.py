class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        arr= [[]]
        for i in range(len(nums)) :
            new_arr = []
            for j in arr :
                copy = j[:]
                copy.append(nums[i])
                new_arr.append(copy)
            for k in  new_arr :
                arr.append(k)
        return arr



            