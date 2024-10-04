class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        word=s.split()
        for i in word:
            res.append(i[::-1])
        return ' '.join(res)
        
