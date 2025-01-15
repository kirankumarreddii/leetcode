class Solution:
    def myAtoi(self, s: str) -> int:
        res=''
        i=0
        s=s.lstrip()
        if i<len(s) and (s[i]=="+" or s[i]=="-"):
            res+=s[i]
            i+=1
        while i<len(s):
            if s[i].isdigit():
                res+=s[i]
            else:
                break
            i+=1
        if res in ('+','-',''):
            return 0
        
        res1=int(res)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if res1>INT_MAX:
            return INT_MAX
        elif res1<INT_MIN:
            return INT_MIN
        else:
            return res1
            
            