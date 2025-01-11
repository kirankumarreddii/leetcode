class Solution:
    def reverseWords(self, s: str) -> str:
        res=[]
        l=0
        word=""
        while l<len(s):
            if s[l]!=' ':
                while l<len(s) and s[l]!=' ':
                    word+=s[l]
                    l+=1
                print(word)
                res.append(word)
                word=""
            l+=1
        return " ".join(res[::-1])
