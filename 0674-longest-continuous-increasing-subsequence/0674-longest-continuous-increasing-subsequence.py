class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        length=1
        count=1
        i=0
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                count+=1
                i+=1
                length=max(count,length)
                continue
            else:
                count=1
            i+=1
        return length


                