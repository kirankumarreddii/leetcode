class StringIterator:

    def __init__(self, compressedString: str):
        self.index=0
        self.count=0
        self.cur_s=''
        self.compressedString=compressedString
                   
    def next(self) -> str:
        if not self.hasNext():
            return " "

        if self.count==0:
                self.cur_s=self.compressedString[self.index]
                self.index+=1
                s=''
                while self.index<len(self.compressedString) and self.compressedString[self.index].isdigit():
                    s+=self.compressedString[self.index]
                    self.index+=1
                self.count=int(s)
        self.count-=1
        return self.cur_s

    def hasNext(self) -> bool:
        if self.count>0 or self.index < len(self.compressedString):
            return True
        
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()