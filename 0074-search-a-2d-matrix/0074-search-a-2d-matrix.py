class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        i = 0
        j = rows*columns-1
        while i<=j:
            mid = (i+j)//2
            r = mid//columns
            c = mid%columns
            if matrix[r][c] == target :
                return True
            elif matrix[r][c] <target:
                i = mid+1
            else : 
                j = mid-1
        return False
