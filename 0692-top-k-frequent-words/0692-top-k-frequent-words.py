class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dici = {}
        ans = []
        for i in words :
            dici[i] = dici.get(i,0)+1
        print(dici)
        # li = sorted(dici,key = dici.get,reverse = True)
        li = sorted(dici, key=lambda word: (-dici[word], word))
        print(li)
        for i in range(k):
            ans.append(li[i])
        return ans 



        