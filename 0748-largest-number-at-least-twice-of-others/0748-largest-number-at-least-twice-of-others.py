class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        a=max(nums)
        maxid=nums.index(a)
        
        for i in nums:
            if a<2*i and i!=a:
                return -1
        return maxid