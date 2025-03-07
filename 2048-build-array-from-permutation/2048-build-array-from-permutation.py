class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        numb=nums[:]
        for i in range(len(numb)):
            numb[i]=nums[nums[i]]
        return numb