class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        sub=[]
        n=len(nums)
        def track(i):
            if i==n:
                res.append(sub[:])
                return
            track(i+1)
            sub.append(nums[i])
            track(i+1)
            sub.pop()
        track(0)
        return res