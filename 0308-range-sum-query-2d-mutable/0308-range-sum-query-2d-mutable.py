class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.Row=len(matrix)
        self.Col=len(matrix[0])
        self.matrix=matrix
        self.Pref_Sum=[[0] *(self.Col+1) for _ in range(self.Row+1)]

        for r in range(self.Row):
            for c in range(self.Col):
                self.Pref_Sum[r+1][c+1]=matrix[r][c]+self.Pref_Sum[r+1][c]+self.Pref_Sum[r][c+1]-self.Pref_Sum[r][c]


    def update(self, row: int, col: int, val: int) -> None:
        dif=val-self.matrix[row][col]
        self.matrix[row][col]=val
        for r in range(row+1,self.Row+1):
            for c in range(col+1,self.Col+1):
                self.Pref_Sum[r][c]+=dif
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (self.Pref_Sum[row2+1][col2+1]+self.Pref_Sum[row1][col1]-self.Pref_Sum[row2+1][col1]-self.Pref_Sum[row1][col2+1])
    
    # def __init__(self, matrix: List[List[int]]):
    #     self.matrix=matrix

    # def update(self, row: int, col: int, val: int) -> None:
    #     self.matrix[row][col]=val
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     sum=0
    #     for r in range(row1,row2+1):
    #         for c in range(col1,col2+1):
    #             sum+=self.matrix[r][c]
    #     return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)