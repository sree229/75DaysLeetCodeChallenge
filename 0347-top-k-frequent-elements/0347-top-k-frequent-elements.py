class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        for i in nums :
            dic[i] = dic.get(i,0) + 1
        dic = sorted(dic,key = dic.get,reverse = True)
        return dic[:k]
