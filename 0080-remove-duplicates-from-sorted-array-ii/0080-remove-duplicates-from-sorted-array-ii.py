class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return 1
        left,right=0,1
        count=1
        while right<len(nums):
            if nums[right]!=nums[right-1]:
                    if count==1:
                        nums[left]=nums[right-1]
                        left+=1
                    else:
                        nums[left]=nums[right-1]
                        left+=1
                        nums[left]=nums[right-1]
                        left+=1
                    count=1
            else:
                count+=1
            right+=1
        if nums[-2]==nums[-1]:
            nums[left]=nums[-1]
            left+=1
            nums[left]=nums[right-1]
            left+=1
        else:
            nums[left]=nums[right-1]
            left+=1
        return left

                
