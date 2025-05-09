class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums
        self.original=nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        n=len(self.nums)
        for i in range(n):
            s=random.randrange(i,n)
            self.nums[i],self.nums[s]=self.nums[s],self.nums[i]
        return self.nums
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()