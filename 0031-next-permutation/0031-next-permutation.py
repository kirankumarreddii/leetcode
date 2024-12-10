class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                index=i-1
                break
        if index == -1:
            nums.reverse()
            return
        for j in range(len(nums)-1,index,-1): 
            if nums[index]<nums[j]:
                nums[index],nums[j]=nums[j],nums[index]
                break
        nums[index+1:]=reversed(nums[index+1:])
        

        