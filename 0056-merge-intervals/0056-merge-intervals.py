class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        arr = []
        curr = intervals[0]
        i = 1
        while i < len(intervals):
            if curr[1] >= intervals[i][0]:
                #  arr.append(curr[0],max(curr[1],intervals[i+1][1])])
                 curr = [curr[0],max(curr[1],intervals[i][1])]
            else :
                arr.append(curr)
                curr = [intervals[i][0],intervals[i][1]]
            i+=1
        arr.append(curr)
        return arr

                



