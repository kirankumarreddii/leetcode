class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s_len=len(s)
        t_len=len(t)
        for i in range(min(s_len,t_len)):
            if s[i]!=t[i]:
                if s_len==t_len:
                    return s[i+1:]==t[i+1:]
                elif s_len>t_len:
                    return s[i+1:]==t[i:]
                else:
                    return s[i:]==t[i+1:]
        return abs(s_len-t_len)==1
            