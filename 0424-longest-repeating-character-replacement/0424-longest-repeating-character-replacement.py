class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        res=0
        j=0
        for i in range(len(s)):
            count[s[i]]+=1
            max_freq=max(count.values())
            cur=i-j+1
            if cur-max_freq>k:
                count[s[j]]-=1
                j+=1
            res=max(res,i-j+1)
        return res
