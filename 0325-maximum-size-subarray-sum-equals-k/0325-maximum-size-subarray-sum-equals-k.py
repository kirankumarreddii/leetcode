class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum={0:-1}
        total=0
        max_sub=0
        for i,num in enumerate(nums):
            total+=num
            if total-k in prefix_sum:
                max_sub=max(max_sub,i-prefix_sum[total-k])
            if total not in prefix_sum:
                prefix_sum[total]=i
        return max_sub