class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res=[]
        i=0
        while i<len(s):
            past=i
            count=1
            while i+1<len(s) and s[i]==s[i+1]:
                count+=1
                i+=1
            if count>=3:
                res.append([past,i])
            i+=1
        return res
                
