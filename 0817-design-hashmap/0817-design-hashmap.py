class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.bucket=[[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        hash_key=key%self.size
        for i ,(k,v) in enumerate(self.bucket[hash_key]):
            if k==key:
                self.bucket[hash_key][i]=(key,value)
                return
    
        self.bucket[hash_key].append((key,value))
        
    def get(self, key: int) -> int:
        hash_key=key%self.size
        for k,v in self.bucket[hash_key]:
            if k == key:
                return v

        return -1 


    def remove(self, key: int) -> None:
        hash_key=key%self.size
        for i,(k,v) in enumerate(self.bucket[hash_key]):
            if k == key:
                del self.bucket[hash_key][i]
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)