class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        dp0=nums[0]
        dp1=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            temp=max(dp0+nums[i],dp1)
            dp0=dp1
            dp1=temp

        return dp1