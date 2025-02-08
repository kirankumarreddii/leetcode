class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        lenth=start=0
        for i in range(len(s)):
            if s[i] in dic and start<=dic[s[i]]:
                start=dic[s[i]]+1
            dic[s[i]]=i
            lenth=max(lenth,i+1-start)
        return lenth 