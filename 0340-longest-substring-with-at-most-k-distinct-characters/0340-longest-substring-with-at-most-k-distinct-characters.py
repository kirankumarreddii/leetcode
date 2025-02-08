class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        dist={}
        start=0
        max_len=0
        for i in range(len(s)):
            dist[s[i]]=dist.get(s[i],0)+1
            while len(dist)>k:
                dist[s[start]]-=1
                if dist[s[start]]==0:
                    dist.pop(s[start])
                start+=1
            max_len=max(max_len,i+1-start)
        return max_len
            