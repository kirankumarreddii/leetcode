class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n=len(citations)
        bucket=[0]*(n+1)
        for i in citations:
            if i>=n:
                bucket[n]+=1
            else:
                bucket[i]+=1
        total=0
        for i in range(n,-1,-1):
            total+=bucket[i]
            if total>=i:
                return i
        return n
