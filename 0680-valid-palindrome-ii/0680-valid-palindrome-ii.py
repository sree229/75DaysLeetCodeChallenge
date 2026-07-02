class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (
                    isPalindrome(left + 1, right) or
                    isPalindrome(left, right - 1)
                )
            left += 1
            right -= 1

        return True
        # if len(s)<2:
        #     return True
        # for i in range(len(s)):
        #     print(i)
        #     if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
        #         return True
        # return False
        # i = 0
        # j = len(s)-1
        # count = 0
        # while i<j:
        #     if s[i]!= s[j] :
        #         if count==1:
        #             return False
        #         else :
        #             count+=1
        #     i+=1
        #     j-=1
        # return Tru
 
