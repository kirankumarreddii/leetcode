class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber_house(arr):
            n=len(arr)
            dp=[0]*2
            dp[0]=arr[0]
            dp[1]=max(arr[0],arr[1])
            for i in range(2,n):
                temp=max(arr[i]+dp[0],dp[1])
                dp[0]=dp[1]
                dp[1]=temp
            return dp[1]
        
        n=len(nums)
        if len(nums)<=3:
            return max(nums)
        max1=robber_house(nums[:-1])
        max2=robber_house(nums[1:])
        return max(max1,max2)
