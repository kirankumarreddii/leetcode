class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        min_val=1
        max_val=1
        for num in nums:
            if num==0:
                min_val=1
                max_val=1
            t=max_val
            max_val=max(t*num,min_val*num,num)
            print(max_val)
            min_val=min(t*num,min_val*num,num)
            print(min_val)
            res=max(max_val,res)
        return res