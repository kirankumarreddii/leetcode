class Solution:
    def countAndSay(self, n: int) -> str:
        res='1'
        if n==1:
            return res
        for i in range(2,n+1):
            temp=''
            j=1
            count=1
            while j<len(res):
                if res[j]==res[j-1]:
                    count+=1
                    j+=1
                    continue
                else:
                    temp+=str(count)+res[j-1]
                    count=1
                j+=1
            temp+=str(count)+res[-1]
            res=temp
        return res


        