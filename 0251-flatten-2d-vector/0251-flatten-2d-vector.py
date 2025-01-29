class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.row=0
        self.col=0
        self.vec=vec

    def next(self) -> int:
        if not self.hasNext():
            raise Exception("No more elements")
        res= self.vec[self.row][self.col]
        self.col+=1
        return res
            
    def hasNext(self) -> bool:
        while self.row<len(self.vec) and self.col>=len(self.vec[self.row]):
            self.col=0
            self.row+=1

        return self.row<len(self.vec)
# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()