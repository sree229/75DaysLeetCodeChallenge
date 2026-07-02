class Solution:
    def validPalindrome(self, s: str) -> bool:
        # def isPalindrome(left, right):
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True

        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return (
        #             isPalindrome(left + 1, right) or
        #             isPalindrome(left, right - 1)
        #         )
        #     left += 1
        #     right -= 1

        # return True
        def ispalindrome(left,right):
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True
        i = 0
        j = len(s)-1
        count = 0
        while i<j:
            if s[i]!= s[j] :
               return ispalindrome(i+1,j) or ispalindrome(i,j-1)
            i+=1
            j-=1
        return True
 
