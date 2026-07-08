from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
    #     if len(t) > len(s):
    #         return ""
    #     sub  = []
    #     for i in range(len(s)) :
    #         for j in range(i,len(s)) :
    #             arr = ""
    #             for k in range(i,j+1):
    #                 arr+= s[k]
    #             sub.append(arr)
    #     st = ""
    #     min_length = 9999
    #     t_counter = Counter(t)
    #     for i in sub:
    #         s_counter = Counter(i)
    #         for key in t_counter :
    #             if t_counter[key] > s_counter[key]:
    #                 flag = 0
    #                 break
    #             else :
    #                 flag =1 
    #         if flag and min_length >len(i) :
    #             st = i 
    #             min_length = len(i)
    #     return st
        if len(t) > len(s):
            return ""
        t_counter = Counter(t)
        s_counter = Counter(s[:len(t)]) 
        windows = s[:len(t)]
        best = "" 
        min_len = 0
        l = 0
        r = len(t)-1 
        matched = 0
        for key in t_counter :
            if s_counter[key] >= t_counter[key] :
                matched+=1
        if matched == len(t_counter) :
            return windows
        while r < len(s)-1:
            r+=1
            windows+= s[r]
            s_counter[s[r]] +=1
            matched = 0
            for key in t_counter :
                if s_counter[key] >= t_counter[key] :
                    matched+=1
            while matched == len(t_counter) :
                if len(windows) < min_len or min_len ==0:
                    best = windows 
                    min_len = len(windows)
                windows = windows[1:]
                s_counter[s[l]] -=1
                l+=1 
                matched = 0
                for key in t_counter:
                    if s_counter[key] >= t_counter[key]:
                        matched += 1
         
        return best

            



                
        