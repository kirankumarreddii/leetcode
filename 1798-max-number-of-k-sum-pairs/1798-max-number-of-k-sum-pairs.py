class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs=Counter(nums)
        count=0
        for num in nums:
            if k-num in pairs:
                if pairs[k-num]>0:
                    count+=1
                    pairs[k-num]-=1
        return count//2
