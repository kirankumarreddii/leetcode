class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        Zero=False
        for num in nums:
            if num==0:
                if not Zero:
                    Zero=True
                else:
                    for i in range(len(nums)):
                        nums[i]=0
                    return nums
            else:
                prod*=num
        if Zero:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=prod
                else:
                    nums[i]=0
        else:
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=prod
                else:
                    nums[i]=prod//nums[i]
        return nums
