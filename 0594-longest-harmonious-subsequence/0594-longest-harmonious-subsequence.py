class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count=Counter(nums)
        tar=0
        for num,freq in count.items():
            if num+1 in count:
                tar=max(tar,freq+count[num+1])
        return tar

        

            
