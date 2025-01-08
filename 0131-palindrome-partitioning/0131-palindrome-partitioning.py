class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def CheckPalindrome(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        def BackTrack(i,path):
            if i==len(s):
                res.append(path[:])
                return
            for j in range(i,len(s)):
                if CheckPalindrome(i,j):
                    path.append(s[i:j+1])
                    BackTrack(j+1,path)
                    path.pop()
        BackTrack(0,[])
        return res