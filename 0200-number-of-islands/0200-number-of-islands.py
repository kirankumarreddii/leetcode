class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count=0
        def track(i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or (i, j) in visited or grid[i][j] == "0":
                return 
            visited.add((i,j))
            track(i+1,j)
            track(i-1,j)
            track(i,j-1)
            track(i,j+1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]== "1" and (i, j) not in visited:
                
                    track(i,j)
                    count+=1
        return count
# from typing import List

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         visited = set()
#         count = 0

#         # Depth-First Search function to track and mark cells
#         def track(i, j):
#             if (i < 0 or i >= len(grid) or      # Out-of-bounds check
#                 j < 0 or j >= len(grid[0]) or   # Out-of-bounds check
#                 (i, j) in visited or            # Already visited check
#                 grid[i][j] == "0"):             # Water cell check
#                 return
            
#             visited.add((i, j))  # Mark this cell as visited

#             # Explore in 4 directions (no diagonals)
#             track(i + 1, j)  # Down
#             track(i - 1, j)  # Up
#             track(i, j + 1)  # Right
#             track(i, j - 1)  # Left

#         # Iterate through each cell in the grid
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == "1" and (i, j) not in visited:
#                     track(i, j)  # Start DFS from this cell
#                     count += 1   # Increment island count

#         return count
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0

        # Depth-First Search function to track and mark cells
        def track(i, j):
            if (i < 0 or i >= len(grid) or      # Out-of-bounds check
                j < 0 or j >= len(grid[0]) or   # Out-of-bounds check
                (i, j) in visited or            # Already visited check
                grid[i][j] == "0"):             # Water cell check
                return
            
            visited.add((i, j))  # Mark this cell as visited

            # Explore in 4 directions (no diagonals)
            track(i + 1, j)  # Down
            track(i - 1, j)  # Up
            track(i, j + 1)  # Right
            track(i, j - 1)  # Left

        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    track(i, j)  # Start DFS from this cell
                    count += 1   # Increment island count

        return count
