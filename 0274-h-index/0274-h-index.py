class Solution:
    def hIndex(self, citations: List[int]) -> int:
        bucket=[0]*(len(citations)+1)
        for c in citations:
            if c>=len(citations):
                bucket[len(citations)]+=1
            else:
                bucket[c]+=1
        total_papers=0
        for i in range(len(citations),-1,-1):
            total_papers+=bucket[i]
            if total_papers>=i:
                return i
        return 0