class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def tracking(idx,path):
            if len(path)==k and sum(path)==n:
                res.append(path[:])
                return 
            if len(path)>k or sum(path)>n:
                return 
            for i in range(idx,10):
                path.append(i)
                tracking(i+1,path)
                path.pop()
        tracking(1,[])
        return res