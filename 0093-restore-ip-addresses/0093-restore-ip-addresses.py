class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        stng=''
        dot=0
        def track(s,dot,stng):
            if len(s)==0 and dot==4:
                res.append(stng[:-1])
                return 
            if len(s)==0 or dot==4:
                return 
            for i in range(3):
                if dot>4 or i+1>len(s):
                    break
                if int(s[:i+1])>255 or (s[0]=='0' and i!=0):
                    continue
                track(s[i+1:],dot+1,stng+s[:i+1]+'.')
                
        track(s,dot,stng)
        return res