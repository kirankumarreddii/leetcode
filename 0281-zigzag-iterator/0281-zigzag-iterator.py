class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.len_v1=len(v1)
        self.len_v2=len(v2)
        self.i=self.j=0
        self.count=0
        self.res=[]
        self.v1=v1
        self.v2=v2
    def next(self) -> int:
        if not self.hasNext():
            raise Exception("No more elements")
        if self.count==0 and self.i<self.len_v1 or (self.j>=self.len_v2):
            cur= self.v1[self.i]
            self.i+=1
                
        else:
            cur= self.v2[self.j]
            self.j+=1
        self.count=1-self.count

        
        return cur

    def hasNext(self) -> bool:
        return self.j<self.len_v2 or self.i<self.len_v1
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())