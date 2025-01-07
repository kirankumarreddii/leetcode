class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited=set()
        rows=len(board)
        cols=len(board[0])
        def Track(row,col):
            if row<0 or col<0 or row>rows-1 or col>cols-1 or board[row][col]=="X" or (row,col) in visited:
                return 
            visited.add((row,col))
            board[row][col]="S"
            Track(row-1,col)
            Track(row+1,col)
            Track(row,col-1)
            Track(row,col+1)


        for row in range(rows):
            for col in range(cols):
                if (row==0 or col==0 or row==rows-1 or col==cols-1) and board[row][col]=="O":
                    Track(row,col)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col]=="S":
                    board[row][col]="O"
                elif board[row][col]=="O":
                    board[row][col]="X"
                