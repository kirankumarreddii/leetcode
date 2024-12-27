class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def track(i,sub):
            if i==len(nums):
                res.append(sub[:])
                return
            sub.append(nums[i])
            track(i+1,sub)
            sub.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            track(i+1,sub)
            

        track(0,[])
        return res