class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final = [[1]]
        prev = [1]
        for i in range(1,numRows) :
            curr = []
            curr.append(1)
            for j in range(len(prev)-1):
                curr.append(prev[j]+prev[j+1])
            curr.append(1)
            prev = curr
            final.append(curr)
        return final



