class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        for a,b in zip(sentence1,sentence2):
            if a==b:
                continue
            if [a,b] not in similarPairs and [b,a] not in similarPairs:
                return False
        return True
