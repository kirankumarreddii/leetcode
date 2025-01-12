class Solution:
    def findMin(self, nums: List[int]) -> int:

        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[left]<=nums[mid]<=nums[right]:
                return nums[left]
            elif nums[mid]<nums[right]:
                right=mid
            else:
                left=mid+1
