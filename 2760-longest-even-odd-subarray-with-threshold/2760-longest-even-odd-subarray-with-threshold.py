class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
            length = 0
            steps = 0
            while steps<len(nums):
                begin = -1
                for start in range(steps,len(nums)):
                    if nums[start]%2==0 and nums[start]<=threshold :
                        begin = start
                        break
                if begin!=-1:
                    i = begin
                    while i<len(nums)-1:
                        if  nums[i]<=threshold and  nums[i] % 2 != nums[i + 1] % 2 :
                            i+=1
                        else :
                            break
                    end = i if nums[i]<=threshold else i-1
                    count = 0
                    for i in range(begin,end+1):
                        count+=1
                    if count > length:
                        length = count
                else :
                    return length
                steps = begin+1
            return length







  # def Find(self,nums,val):
    #     for i in range(len(nums)):
    #         if nums[i]%2==0 and nums[i]<=val:
    #             return i
    #     return None
# l = self.Find(nums,threshold)
        # if l == len(nums)-1:
        #     return 1
        # l1 = []
        # count = 0
        # r = l+1
        # while r<len(nums):
        #     for i in range(l,r):
        #         if  nums[i] % 2 != nums[i + 1] % 2 and nums[i]<=threshold:
        #             l1.append(i)
        #         else :

        #     if len(l1)>count:
        #         count = len(l1)
        # count = 0
        # l1 = []
        # start = self.Find()
        # if start == None:
        #     return 0
        # if start == len(nums)-1:
        #     return 1
        # end = start+1
        # while end<len(nums):
        #         for i in range(start,end):
        #             if  nums[i] % 2 != nums[i + 1] % 2 and nums[i]<=threshold:
        #                 l1.append(i)
        #         end+=1










