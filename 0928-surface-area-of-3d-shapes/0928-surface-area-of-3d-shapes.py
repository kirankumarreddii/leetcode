class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        surface_area = 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    surface_area += 2
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n:
                            neighbor = grid[ni][nj]
                        else:
                            neighbor = 0
                        surface_area += max(grid[i][j] - neighbor, 0)
                        
        return surface_area
