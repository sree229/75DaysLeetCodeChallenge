class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        seen = {}  
        max_length = 0
        while right<len(s):
            char = s[right]
            if char  in seen:
                old_left = left
                left =  seen[char]+1
                for i in range(old_left,left):
                    del seen[s[i]]
            seen[char] = right 
            if len(seen) > max_length :
                max_length = len(seen)
            right +=1
        return max_length