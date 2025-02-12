class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        point=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[point]=nums[i]
                point+=1
        for i in range(point,len(nums)):
            nums[i]=0
            