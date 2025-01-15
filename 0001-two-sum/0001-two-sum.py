class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist={}
        for i in range(len(nums)):
            if (target-nums[i]) not in dist:
                dist[nums[i]]=i
            else:
                return [i,dist[target-nums[i]]]