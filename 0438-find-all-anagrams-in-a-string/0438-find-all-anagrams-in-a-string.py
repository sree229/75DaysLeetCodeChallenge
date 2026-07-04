from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]: 
        if  len(p) > len(s) :
            return []
        arr = []
        s_count = Counter(s[:len(p)])
        p_count = Counter(p)
        if s_count == p_count:
            arr.append(0)
        for left in range(len(s)-len(p)):
            right_char = s[left+len(p)]
            s_count[right_char]+=1
            left_char = s[left]
            s_count[left_char]-=1
            if s_count[left_char] == 0:
                del s_count[left_char]
            if s_count == p_count:
                arr.append(left+1)
        return arr
