class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res=0
        cols=len(grid[0])
        rows=len(grid)
        for i in range(1,cols):
            grid[0][i]+=grid[0][i-1]
        for j in range(1,rows):
            grid[j][0]+=grid[j-1][0]
        for r in range(1,rows):
            for c in range(1,cols):
                grid[r][c]+=min(grid[r][c-1],grid[r-1][c])
        return grid[rows-1][cols-1]
