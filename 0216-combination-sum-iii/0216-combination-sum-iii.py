class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def tracking(idx,path,target):
            if len(path)==k and target==n:
                res.append(path[:])
                return 
            if len(path)>k or target>n:
                return 
            for i in range(idx,10):
                path.append(i)
                tracking(i+1,path,target+i)
                path.pop()
        tracking(1,[],0)
        return res