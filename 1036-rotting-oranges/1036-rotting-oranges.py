class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=-1
        fresh=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh == 0:
            return 0
                
        while queue:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for i,j in [(0,-1),(0,1),(-1,0),(1,0)]:
                    r_i=r+i
                    c_j=c+j
                    if 0<=r_i<len(grid) and 0<=c_j<len(grid[0]) and grid[r_i][c_j]==1:
                        grid[r_i][c_j]=2
                        queue.append((r_i,c_j))
                        fresh-=1
                
            count+=1
        return count if fresh==0 else -1
