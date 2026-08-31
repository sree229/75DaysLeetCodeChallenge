class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        li = []
        for i in range(len(points)) :
            val = sqrt((points[i][0]*points[i][0])+(points[i][1]*points[i][1]))
            li.append([val,i])
        li = sorted(li,key = lambda x : x[0])
        print(li)
        res = []
        i = 0 
        while i < k:
            res.append(points[li[i][1]])
            i+=1
        return res

        