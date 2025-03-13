class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def tracking(indx,path,total):
            if len(path)==k and total==n:
                res.append(path[:])
                return 
            if len(path)>k or total>n:
                return 
            for i in range(indx,10):
                path.append(i)
                tracking(i+1,path,total+i)
                path.pop()
        tracking(1,[],0)
        return res