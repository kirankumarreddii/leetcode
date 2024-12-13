class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def track(start,target,path):
            if target==0:
                res.append(path[:])
                return
            if target<0:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                track(i,target-candidates[i],path)
                path.pop()
       
        track(0,target,[])
        return res