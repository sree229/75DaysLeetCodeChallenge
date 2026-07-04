class Solution:
    def countSubstrings(self, s: str) -> int:
        # count = 0
        # for i in range(len(s)):
        #     for  j in range(i,len(s)):
        #         sub_array = []
        #         for k in range(i,j+1) :
        #             sub_array.append(s[k])
        #         if sub_array == sub_array[::-1]:
        #                 count +=1
        # return count
        count = 0
        for i in range(len(s)):
            left = i
            right = i
            while left>=0 and right< len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
            left = i
            right = i+1
            while left>=0 and right< len(s) and s[left]==s[right]:
                count+=1
                left-=1
                right+=1
        return count

        