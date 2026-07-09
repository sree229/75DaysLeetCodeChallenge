class Solution:
    def reverse(self,n,i,j) :
        while i<j :
            n[i] , n[j] = n[j],n[i]
            i+=1
            j-=1
        return n
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        d = len(nums)-k
        nums =  self.reverse(nums,0,d-1)
        nums =  self.reverse(nums,d,len(nums)-1)
        nums =  self.reverse(nums,0,len(nums)-1)
    