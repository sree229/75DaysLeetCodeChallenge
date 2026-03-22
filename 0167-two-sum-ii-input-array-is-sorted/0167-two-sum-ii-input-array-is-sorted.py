class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen = {}
        # for index,num in enumerate(numbers) :
        #     d = target-num
        #     if d in seen:
        #             return seen[d]+1,index+1
        #     seen[num] = index
        # return None
        seen = {}
        for i in range(len(nums)):
            d = target - nums[i]
            if d in seen:
                return seen[d],i+1
            else:
                seen[nums[i]] = i+1
        return None












