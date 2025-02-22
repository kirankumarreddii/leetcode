class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber_house(arr):
            n=len(arr)
            prev=arr[0]
            cur=max(arr[0],arr[1])
            for i in range(2,n):
                temp=max(arr[i]+prev,cur)
                prev,cur=cur,temp
            return cur
        
        n=len(nums)
        if len(nums)<=3:
            return max(nums)
        max1=robber_house(nums[:-1])
        max2=robber_house(nums[1:])
        return max(max1,max2)
