class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = []
        for i in range(len(matrix)):
            j = len(matrix)-1
            m1 = []
            while j>=0:
                m1.append(matrix[j][i])
                j-=1
            m.append(m1)
        for i in range(len(m)):
            for j in range(len(m)):
                matrix[i][j] = m[i][j]




  
        