from operator import itemgetter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        sorted_d = dict(sorted(d.items(), key=itemgetter(1),reverse=True))
        dq = [ key for key in sorted_d]
        dq = dq[:k:]
        return dq

        
            
