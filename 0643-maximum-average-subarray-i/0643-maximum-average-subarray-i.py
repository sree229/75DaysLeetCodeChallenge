class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 1
        windows_sum = sum(nums[0:k])
        avg = windows_sum/k
        while i<len(nums)-k+1 :
            windows_sum  = windows_sum - nums[i-1]+nums[i+k-1]
            value = windows_sum/k
            if value> avg:
                avg = value
            i+=1
        return avg