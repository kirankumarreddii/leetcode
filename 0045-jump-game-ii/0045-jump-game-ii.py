class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        left=right=0
        while right<len(nums)-1:
            reach=0
            while left<=right:
                reach=max(reach,left+nums[left])
                left+=1
            right=reach
            jump+=1
        return jump

    