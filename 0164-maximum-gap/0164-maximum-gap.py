class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        min_val=min(nums)
        max_val=max(nums)
        n=len(nums)
        bucket_size=max(1,(max_val-min_val)//(n-1))
        bucket_count=(max_val-min_val)//bucket_size+1
        bucket_list=[[float('inf'),float('-inf')] for _ in range(bucket_count)]
        for num in nums:
            bucket_indx=(num-min_val)//bucket_size
            bucket_list[bucket_indx][0]=min(bucket_list[bucket_indx][0],num)
            bucket_list[bucket_indx][1]=max(bucket_list[bucket_indx][1],num)
        max_gap=0
        pre_val=min_val
        for mini,maxi in bucket_list:
            if mini==float('inf') and maxi==float('-inf'):
                continue
            max_gap=max(mini-pre_val,max_gap)
           
            pre_val=maxi
        return max_gap
