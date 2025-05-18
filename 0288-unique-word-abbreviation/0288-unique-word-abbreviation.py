class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.map = defaultdict(set)
        self.words=set(dictionary)
        for word in self.words:
            con=self.convert(word)
            self.map[con].add(word)
    def isUnique(self, word: str) -> bool:
        con=self.convert(word)
        return con not in self.map or self.map[con]=={word}
    def convert(self,letter):
        if len(letter)<=2:
            return letter
        return letter[0]+str(len(letter)-2)+letter[-1]

        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)