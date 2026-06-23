class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # sum = nums[0]
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         prev_sum = 0
        #         for k in range(i,j+1):
        #             prev_sum+=nums[k]
        #         if prev_sum >sum:
        #             sum = prev_sum
        # return sum
        curr_sum = nums[0]
        max_sum  = nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i],curr_sum+nums[i])
            max_sum = max(max_sum,curr_sum)  
        return max_sum    


        