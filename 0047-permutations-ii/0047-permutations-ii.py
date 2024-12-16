class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def track(used,path):
            if len(path)==len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i] or (nums[i]==nums[i-1] and i>0) and not used[i - 1] :
                    continue
                used[i]=True
                path.append(nums[i])
                track(used,path)
                used[i]=False
                path.pop()
        track([False]*len(nums),[])
        return res
