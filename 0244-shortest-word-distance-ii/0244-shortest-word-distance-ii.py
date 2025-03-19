class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.store=defaultdict(list)

        for i,di in enumerate(wordsDict):
            self.store[di].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        mini=float('inf')
        # for i in self.store[word1]:
        #     for j in self.store[word2]:
        indx1=self.store[word1]
        indx2=self.store[word2]
        i=j=0
        while i<len(indx1) and j<len(indx2):
            mini=min(mini,abs(indx1[i]-indx2[j]))
            if indx1[i]<indx2[j]:
                i+=1
            else:
                j+=1
        return mini




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)