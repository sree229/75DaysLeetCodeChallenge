from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        s2_count = Counter(s2[:len(s1)])
        if s1_count == s2_count :
            return True
        for left in range(len(s2)-len(s1)):
            right = s2[left+len(s1)]
            s2_count[right] += 1
            left_ch = s2[left]
            s2_count[left_ch]-=1
            if s2_count[left_ch] == 0:
                del s2_count[left_ch]
            if s1_count == s2_count :
                return True
        return False
            
