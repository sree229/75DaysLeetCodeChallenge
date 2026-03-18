class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l = [0]*len(nums)
        # for i in range(len(nums)):
        #     mul = 1
        #     for j in range(len(nums)) :
        #         if j ==i:
        #             pass
        #         else:
        #             mul*=nums[j]
        #     l[i] = mul
        # return l
        # for i in range(len(nums)):
        #     l = nums[:i:]+nums[i+1::]
        #     mul = 1
        #     res = [mul for i in l mul*=i]
        # print(res)
        n = len(nums)
        answer = [1] * n
        for i in range(1, n):
             answer[i] = answer[i-1] * nums[i-1]
        right = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        return answer


        