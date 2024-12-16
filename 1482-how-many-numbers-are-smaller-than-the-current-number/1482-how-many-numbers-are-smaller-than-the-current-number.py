class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        dist={}

        for idx,val in enumerate(temp):
            if temp[idx] not in dist:
                dist[temp[idx]]=idx
        res=[]
        for i in range(len(nums)):
            res.append(dist[nums[i]])
        return res