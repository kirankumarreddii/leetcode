class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        pref_sum=defaultdict(int)
        pref_sum[0]=1
        com_sum=0
        for num in nums:
            com_sum+=num
            count+=pref_sum[com_sum-k]
            pref_sum[com_sum]+=1
        return count
                

