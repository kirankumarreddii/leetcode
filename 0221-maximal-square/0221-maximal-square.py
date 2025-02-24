class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        max_length=0
        row=len(matrix)
        col=len(matrix[0])
        for r in range(row):
            for c in range(col):
                matrix[r][c]=int(matrix[r][c])
                max_length=max(max_length,matrix[r][c])
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c]==1:
                    matrix[r][c]=min(matrix[r-1][c-1],matrix[r-1][c],matrix[r][c-1])+1
                    max_length=max(max_length,matrix[r][c])
        return max_length*max_length
        