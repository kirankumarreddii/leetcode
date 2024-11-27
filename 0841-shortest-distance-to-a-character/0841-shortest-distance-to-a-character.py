class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n=len(s)
        dist=[float('inf')]*n
        pos=None
        for i in range(n):
            if s[i]==c:
                pos=i
            dist[i]=i-pos if pos is not None else float('inf')
        

        for i in range(n-1,-1,-1):
            if s[i]==c:
                pos=i
            dist[i]=min(dist[i],abs(pos-i))

        return dist