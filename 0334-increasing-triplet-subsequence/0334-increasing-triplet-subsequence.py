# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         if len(nums)<3:
#             return False
#         second,first=float('inf'),float('inf')
#         for num in nums:
#             if num<=first:
#                 first=num
#             elif second<=num:
#                 second=num
#             else:
#                 return True
#         return False
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  # smallest number so far
            elif num <= second:
                second = num  # second smallest number
            else:
                return True  # found third number greater than both
        
        return False
