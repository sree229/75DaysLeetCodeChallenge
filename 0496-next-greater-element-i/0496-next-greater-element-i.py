class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        while nums1:
            first = nums1.pop()
            top2 = len(nums2)-1
            while first != nums2[top2] :
                top2-=1
            pos = top2
            while top2 != len(nums2) :
                if nums2[top2] > nums2 [pos]:
                    stack.append(nums2[top2])
                    break
                top2+=1
            else :
                stack.append(-1)
        return stack[::-1]
                


                        

                    
        