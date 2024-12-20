class Solution:
    def canJump(self, nums: List[int]) -> bool:
        left=0
        reach=0
        while left<len(nums):
            if left>reach:
                return False
            reach=max(reach,left+nums[left])
            if left>=len(nums)-1:
                return True
            left+=1
        return True