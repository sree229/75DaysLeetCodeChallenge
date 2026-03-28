class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}          # frequency of characters
        left = 0
        maxf = 0            # max frequency in current window
        res = 0
        for right in range(len(s)):
            # add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # update max frequency
            maxf = max(maxf, count[s[right]])

            # check if window is invalid
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1

            # update result
            res = max(res, right - left + 1)

        return res