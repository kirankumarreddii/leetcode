class RandomizedSet:

    def __init__(self):
        self.elements=set()
        self.back=[]

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements.add(val)
        self.back.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.elements:
            self.elements.remove(val)
            idx=self.back.index(val)
            self.back[idx]=self.back[-1]
            self.back.pop()
            return True
        else:
            return False
    def getRandom(self) -> int:
        return random.choice(self.back)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()