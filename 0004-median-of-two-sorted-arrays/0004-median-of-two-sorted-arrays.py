class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        k = 0
        arr = [0]*(len(nums1)+len(nums2))
        while i <  len(nums1) and j <len(nums2) :
            if nums1[i] <= nums2[j]:
                arr[k] = nums1[i]
                i+=1
            else :
                arr[k] = nums2[j]
                j+=1
            k+=1
        while i < len(nums1):
            arr[k]= nums1[i]
            i+=1
            k+=1
        while j<len(nums2):
            arr[k] = nums2[j]
            j+=1
            k+=1
        if len(arr)%2 != 0:
            return arr[len(arr)//2]
        else :
            i = len(arr)//2
            j = i-1
            return  float(arr[i]+arr[j])/2