class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(start,n,path):
            for i in range(start,int(n**0.5)+1):
                if n%i==0:
                    res.append(path+[i,n//i])
                    backtrack(i,n//i,path+[i])
        res=[]
        backtrack(2,n,[])
        return res