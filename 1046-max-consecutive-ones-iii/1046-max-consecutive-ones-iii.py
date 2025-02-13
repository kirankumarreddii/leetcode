class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # last=right=lenth=0

        # while right<len(nums):
        #     if nums[right]==0:
        #         k-=1
        #     while k<0:
        #         if nums[last]==0:
        #             k+=1
        #         last+=1
        #     lenth=max(lenth,right+1-last)
        #     right+=1
        # return lenth
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] == 0:
                k -= 1
            j += 1
            if k < 0:
                if nums[i] == 0:
                    k += 1
                i += 1
        return j - i