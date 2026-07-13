class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0]*len(nums1)
        for i in range(len(nums1)) :
            flag = 0
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] :
                    break
            for k in range(j+1,len(nums2)) :
                if nums2[k] > nums2[j] :
                    ans[i] = nums2[k]
                    flag =1
                    break
            if flag == 0:
                ans[i] = -1
        return ans
                        

                    
        