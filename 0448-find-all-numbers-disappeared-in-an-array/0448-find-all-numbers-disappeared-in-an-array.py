class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # i =1
        # final = []
        # n = len(nums)
        # while i<=n:
        #     if i not in nums :
        #         final.append(i)
        #     i+=1
        # return final
        final = []
        length = len(nums)+1
        index = [0]*length
        index[0] = 1
        for i in nums:
            index[i] = 1
        for i in range(len(index)):
            if index[i] == 0:
                final.append(i)
        return final



