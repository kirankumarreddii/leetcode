class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length=float('inf')
        left=current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            while current_sum>=target:
                min_length=min(min_length,right-left+1)
                current_sum-=nums[left]
                left+=1
        return min_length if min_length!=float('inf') else 0