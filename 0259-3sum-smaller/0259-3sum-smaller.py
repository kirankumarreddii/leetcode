class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count=0
        for i in range(len(nums)-2):
            j=len(nums)-1
            left=i+1
            while left<j:
                if nums[i]+nums[left]+nums[j]<target:
                    count+=(j-left)
                    left += 1
                else:
                    j-=1
        return count
            
            

