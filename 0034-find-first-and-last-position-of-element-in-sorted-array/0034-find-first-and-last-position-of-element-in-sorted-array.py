class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        def binaryl(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(right+left)//2
                if nums[mid]>=target:
                    right=mid-1
                else:
                    left=mid+1
            return left
        def binaryr(nums,target):
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(right+left)//2
                if nums[mid]<=target:
                    left=mid+1
                    
                else:
                    right=mid-1
            return right
        left=binaryl(nums,target)
        right=binaryr(nums,target)
        if left<=right:

            return [left,right]
        return res