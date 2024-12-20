class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for s in strs:
            char_=[0]*26
            for char in s:
                char_[ord(char) - ord("a")]+=1
            key=tuple(char_)
            anagrams[key].append(s)
        return list(anagrams.values())