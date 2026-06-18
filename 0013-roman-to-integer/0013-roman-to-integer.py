class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        def fun(ch):
            if ch == "I":
                return 1
            if ch == "V":
              return 5
            if ch == "X":
                return 10
            if ch == "L":
                return 50
            if ch == "C":
                return 100
            if ch == "D":
                return 500
            if ch == "M":
                return 1000
        for l in range(len(s)-1):
            r = l+1
            if fun(s[l]) < fun(s[r]):
                ans -=fun(s[l])
            else :
                ans += fun(s[l]) 
        ans += fun(s[-1])
        return ans