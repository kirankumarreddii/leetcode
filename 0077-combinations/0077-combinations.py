class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        def track(start,com):
            if len(com)==k:
                res.append(com[:])
                return 
            for i in range(start,n+1):
                com.append(i)
                track(i+1,com)
                com.pop()
        track(1,[])
        return res