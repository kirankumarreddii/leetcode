class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''
        t_count=Counter(t)
        need=len(t_count)
        window_count={}
        l=r=have=0
        min_len=float('inf')
        min_size=(0,0)
        while r<len(s):
            char=s[r]
            if char in t_count:
                window_count[char]=1 + window_count.get(char,0)
                if window_count[char]==t_count[char]:
                    have+=1
            while l<=r and have==need:
                if (r-l+1)<min_len:
                    min_len=r-l+1
                    min_size=(l,r)
                if s[l] in t_count:
                    window_count[s[l]]-=1
                    if window_count[s[l]] < t_count[s[l]]:
                        have-=1
                l+=1
            r+=1

        return '' if min_len==float('inf') else s[min_size[0]:min_size[1]+1]
