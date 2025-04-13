class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        text1=s1.split()+s2.split()
        count=Counter(text1)
        return [word for word,freq in count.items() if freq==1]

