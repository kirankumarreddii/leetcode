class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort() 

        def track(target,path,start):
            if target==0:
                res.append(path[:])
                return 
            if target<0:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                track(target-candidates[i],path,i+1)
                path.pop()
        track(target,[],0)
        return res