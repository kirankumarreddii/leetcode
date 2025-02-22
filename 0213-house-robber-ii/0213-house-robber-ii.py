class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)<=3:
            return max(nums)
        dp=[0]*(n-1)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n-1):
            temp=max(nums[i]+dp[0],dp[1])
            dp[0]=dp[1]
            dp[1]=temp
        max_length=dp[1]
        dp[0]=nums[1]
        dp[1]=max(nums[1],nums[2])
        for i in range(3,n):
            temp=max(nums[i]+dp[0],dp[1])
            dp[0]=dp[1]
            dp[1]=temp
        max_length=max(max_length,dp[1])
        return max_length
