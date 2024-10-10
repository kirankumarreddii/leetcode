class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avge=sum(nums[:k])
        a=avge/k
        for i in range(k,len(nums)):
            avge=avge+nums[i]-nums[i-k]
            a=max(a,(avge/k))
            print("else",a)
        return a