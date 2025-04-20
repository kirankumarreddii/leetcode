class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        queue=deque([])
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j]==0:
                    queue.append((i,j))
        while queue:
            row,col=queue.popleft()
            val=rooms[row][col]+1
            for r,c in [(1,0),(-1,0),(0,-1),(0,1)]:
                new_r=r+row
                new_c=c+col
                if new_r < 0 or new_r >= len(rooms) or new_c < 0 or new_c >= len(rooms[0]):
                    continue
                if val<rooms[new_r][new_c]:
                    rooms[new_r][new_c]=val
                    queue.append((new_r,new_c))
        
