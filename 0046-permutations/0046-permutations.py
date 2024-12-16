class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def track(used,path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    track(used,path)

                    used[i]=False
                    path.pop()
        track([False]*len(nums),[])
        return res
