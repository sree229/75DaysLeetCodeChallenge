class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            s = s[::-1].strip()
            count  = 0
            for i in s :
                if i == " ":
                    break
                count+=1
            return count

        