class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        
        if len(s)==2 and s[0]==s[1] and k==1:
            return False
        if len(s)>=1 and k==1:
            return True
        left=s[0]
        count=0
        for i in range(len(s)):
            if s[i]==left:
                count+=1
                if count==k and i+1<len(s) and s[i+1]==left:
                    continue
                elif count==k:
                    return True
            else:
                count=1
                left=s[i]
        
        return False
