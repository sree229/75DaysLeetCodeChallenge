class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s = s.lower()
        res = ""
        for i in s:
            # if  #97<=ord(i)<=122
            if  i.isalnum():
                res+=i
        print(res)
        if (res==res[::-1]) :
            return True
        else :
            return False
        
        

            