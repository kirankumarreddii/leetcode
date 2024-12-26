class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left,right=1,1
        count=1
        while right<len(nums):
            if nums[right]==nums[right-1]:
                count+=1
            else:
                count=1
            if count<=2:
                nums[left]=nums[right]
                left+=1
            right+=1
        return left
                
