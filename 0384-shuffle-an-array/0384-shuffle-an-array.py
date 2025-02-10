# class Solution:

#     def __init__(self, nums: List[int]):
#         self.nums=nums
#         self.original=nums[:]

#     def reset(self) -> List[int]:
#         return self.original

#     def shuffle(self) -> List[int]:
#         n=len(self.nums)
#         for i in range(n):
#             s=random.randrange(i,n)
#             self.nums[i],self.nums[s]=self.nums[s],self.nums[i]
#         return self.nums
# # Your Solution object will be instantiated and called as such:
# # obj = Solution(nums)
# # param_1 = obj.reset()
# # param_2 = obj.shuffle()
import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]  # Store an immutable copy
        self.nums = nums[:]  # Work on a separate copy

    def reset(self) -> List[int]:
        self.nums = self.original[:]  # Reset to the original copy
        return self.nums

    def shuffle(self) -> List[int]:
        n = len(self.nums)
        for i in range(n):
            s = random.randrange(i, n)
            self.nums[i], self.nums[s] = self.nums[s], self.nums[i]
        return self.nums

# Example usage:
# obj = Solution([1, 2, 3])
# print(obj.shuffle())  # Random order
# print(obj.reset())  # [1, 2, 3]
