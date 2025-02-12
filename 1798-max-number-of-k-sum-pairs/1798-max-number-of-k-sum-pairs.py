class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        pairs=Counter(nums)
        count=0
        # for num in nums:
        #     if k-num in pairs:
        #         if pairs[k-num]>0:
        #             count+=1
        #             pairs[k-num]-=1
        # return count//2
        for num in nums:
            if pairs[num] > 0 and pairs[k - num] > 0:  # Ensure both numbers exist
                if num == k - num and pairs[num] < 2:  # Handle case when num == k - num
                    continue
                count += 1
                pairs[num] -= 1
                pairs[k - num] -= 1  # Reduce count of complement

        return count
