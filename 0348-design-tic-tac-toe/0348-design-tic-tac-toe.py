class TicTacToe:

    def __init__(self, n: int):
        self.n=n
        self.rows=[0]*n
        self.cols=[0]*n
        self.dia=0
        self.O_dia=0
    def move(self, row: int, col: int, player: int) -> int:
        score=1 if player==1 else -1

        self.rows[row]+=score
        self.cols[col]+=score
        if row==col:
            self.dia+=score
        if row+col==self.n-1:
            self.O_dia+=score

        if abs(self.rows[row])==self.n or abs(self.cols[col])==self.n or abs(self.dia)==self.n or abs(self.O_dia)==self.n:
            return player
        return 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)