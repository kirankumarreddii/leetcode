class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # if not matrix or not matrix[0]:
        #     self.matrix = []
        #     return
        
        self.matrix=matrix
        for i in range(1,len(matrix[0])):
            matrix[0][i]+=matrix[0][i-1]
        for j in range(1,len(matrix)):
                matrix[j][0]+=matrix[j-1][0]
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                matrix[i][j]+=matrix[i-1][j]+matrix[i][j-1]- matrix[i-1][j-1]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # self.sum1+=self.matrix[row2][col2]
        # if col1 > 0:
        #     self.sum1+=-self.matrix[row1][col1-1]
        # if row1>0:
        #     self.sum1+=-self.matrix[row1-1][col1]
        # if col1>0 and row1>0:
        #     self.sum1+=self.matrix[row1-1][col1-1]
        # return self.sum1

        sum1 = self.matrix[row2][col2]
        
        if col1 > 0:
            sum1 -= self.matrix[row2][col1-1]  # Subtract the area left of the region
        if row1 > 0:
            sum1 -= self.matrix[row1-1][col2]  # Subtract the area above the region
        if row1 > 0 and col1 > 0:
            sum1 += self.matrix[row1-1][col1-1]  # Add the overlapping area that was subtracted twice
        
        return sum1

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)