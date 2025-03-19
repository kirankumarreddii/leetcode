class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.store=defaultdict(list)

        for i,di in enumerate(wordsDict):
            self.store[di].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        mini=float('inf')
        for i in self.store[word1]:
            for j in self.store[word2]:
                mini=min(mini,abs(i-j))
        return mini




# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)