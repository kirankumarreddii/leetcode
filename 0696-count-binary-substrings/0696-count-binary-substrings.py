class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count=0
        p=0
        c=1
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                c+=1
            else:
                count+=min(p,c)
                p=c
                c=1
        count+=min(p,c)
        return count