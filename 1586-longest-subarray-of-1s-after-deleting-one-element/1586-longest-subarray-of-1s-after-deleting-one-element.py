class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        window=max_length=j=0
        zero=1
        while j<len(nums):
            if nums[j]==0:
                zero-=1
            while zero<0 and window<=j:
                if nums[window]==0:
                    zero+=1
                window+=1
            max_length = max(max_length, j - window)
            j+=1
        return max_length