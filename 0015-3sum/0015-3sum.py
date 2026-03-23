class Solution:
   def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        nums.sort()
        for i in range(len(nums)) :
            a = -nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[right] == a:
                    seen.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif nums[left]+nums[right] < a :
                    left+=1
                else :
                    right-=1
        return [list(t) for t in seen]
        
          




















