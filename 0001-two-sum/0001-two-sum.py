class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dist={}
        for i, num in enumerate(nums):
            if target-num in dist:
                return [dist[target-num],i]
            dist[num]=i         