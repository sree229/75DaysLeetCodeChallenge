class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_sub = ""
        count = 0
        for i in range(len(s)):
            left, right =  i,i
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -=1
                right+=1
            sub1 = s[left+1:right]
            left,right = i,i+1
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -=1
                right+=1
            sub2 = s[left+1:right]
            if max(len(sub1),len(sub2)) > count :
                count = max(len(sub1),len(sub2))
                s_sub = sub1 if len(sub1) > len(sub2) else sub2
        return s_sub
