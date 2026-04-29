class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dicti = {}
        i = 0
        while i<len(nums):
            dicti[nums[i]] = dicti.get(nums[i],0)+1
            d = dicti[nums[i]]
            if d>2:
                nums.pop(i)
            else :
                i+=1
        print(dicti)
        return len(nums)