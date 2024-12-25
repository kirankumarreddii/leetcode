class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        def track(i,j,idx):
            if idx==len(word):
                return True
            if i<0 or j<0 or i>=row or j>=col or board[i][j]!=word[idx]:
                return False
            temp=board[i][j]
            board[i][j]='#'
            found=(track(i-1,j,idx+1) or track(i+1,j,idx+1) or track(i,j-1,idx+1) or track(i,j+1,idx+1))

            board[i][j]=temp
            return found

        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    if track(i,j,0):
                        return True
        return False