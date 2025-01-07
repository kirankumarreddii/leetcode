class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_length=0
        set_nums=set(nums)
        for num in set_nums:
            if num-1 not in set_nums:
                max_len=1
                while num+1 in set_nums:
                    max_len+=1
                    num+=1
                curr_length=max(curr_length,max_len)
        return curr_length