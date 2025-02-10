class RandomizedSet:

    def __init__(self):
        self.elements={}
        self.back=[]

    def insert(self, val: int) -> bool:
        if val in self.elements:
            return False
        self.elements[val]=len(self.back)
        self.back.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.elements:
            idx=self.elements[val]
            last_element=self.back[-1]
            self.back[idx] = last_element
            self.elements[last_element]=idx
            self.back.pop()
            del self.elements[val]
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