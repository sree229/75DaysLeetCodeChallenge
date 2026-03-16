class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # final = []
        # i = 0
        # while i<len(strs):
        #     l = []
        #     l.append(strs[i])
        #     j = i+1
        #     while(j<len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             d = strs.pop(j)
        #             l.append(d)
        #         else:
        #             j+=1
        #     i+=1
        #     final.append(l)
        # return final
        d = {}
        res = []
        for i in strs:
            key = "".join(sorted(i))
            if key not in d:
               d[key] = []
            d[key].append(i)
        for key in d:
            res.append(d[key])
            
        return res
        