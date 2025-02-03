class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # old | new | state
        #  0 | 0 | 0
        #  0 | 1 | 2
        #  1 | 0  | 1
        #  1  | 1 | 3
        def neighbour(r,c):
            nei=0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    
                    if (i==r and j==c) or i<0 or j<0 or i>=Row or j>=Col:
                        continue
                    if board[i][j] in [1,3]:
                        nei+=1
            return nei
        Row=len(board)
        Col=len(board[0])
        for i in range(Row):
            for j in range(Col):
                nei=neighbour(i,j)
                if board[i][j]:
                    if nei in [2,3]:
                        board[i][j]=3
                elif nei==3:
                    board[i][j]=2
        for i in range(Row):
            for j in range(Col):
                if board[i][j] in [2,3]:
                    board[i][j]=1
                elif board[i][j]==1:
                    board[i][j]=0
        

