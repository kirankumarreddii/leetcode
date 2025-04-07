class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        top=sum(cell>0 for row in grid for cell in row)
        side=sum(max(row) for row in grid)
        front=sum(max(col) for col in zip(*grid))
        return top+side+front