class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s1 = set(nums)
        if len(nums) == len(s1):
            return False
        return True
        