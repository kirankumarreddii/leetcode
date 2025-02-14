class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        set1=Counter(word1)
        set2=Counter(word2)
        if set(set1.keys())!=set(set2.keys()):
            return False
        return sorted(set1.values())==sorted(set2.values())