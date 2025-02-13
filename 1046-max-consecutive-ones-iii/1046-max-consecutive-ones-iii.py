class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        last=right=lenth=0

        while right<len(nums):
            if nums[right]==0:
                k-=1
            while k<0:
                if nums[last]==0:
                    k+=1
                last+=1
            lenth=max(lenth,right+1-last)
            right+=1
        return lenth
