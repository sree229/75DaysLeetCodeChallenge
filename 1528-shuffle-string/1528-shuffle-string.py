class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        words = [0]*len(s)
        i = 0
        while i < len(indices):
            pos = indices[i]
            words[pos] = s[i]
            i+=1
        new_s = "".join(words)
        return new_s
    