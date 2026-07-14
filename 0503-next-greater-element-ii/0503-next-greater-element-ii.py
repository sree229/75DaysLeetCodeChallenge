class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = []
        top = 0
        while top < len(nums):
            if top != len(nums)-1:
                item = top+1
            else :
                item = 0
            while item!= top :
                if nums[item] > nums[top] :
                    arr.append(nums[item])
                    break
                elif item == len(nums)-1:
                    item = 0
                else : 
                    item +=1
            else :
                arr.append(-1)
            top +=1
        return arr
        
        