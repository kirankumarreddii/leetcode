# class Solution:
#     def threeSumSmaller(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         count=0
#         for i in range(len(nums)-2):
#             if nums[i]>=target:
#                 break
#             j=len(nums)-1
#             left=i+1
#             while left<j:
#                 if nums[i]+nums[left]+nums[j]<target:
#                     count+=(j-left)
#                     left += 1
#                 else:
#                     j-=1
#         return count
            
            

from typing import List

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()  # Step 1: Sort the array
        count = 0
        n = len(nums)

        for i in range(n - 2):  # Iterate until n-2 to ensure we have triplets
            left, right = i + 1, n - 1  # Two-pointer initialization

            while left < right:
                if nums[i] + nums[left] + nums[right] < target:
                    count += (right - left)  # Count all valid pairs (left, left+1, ..., right)
                    left += 1  # Move left to find more valid pairs
                else:
                    right -= 1  # Reduce right to try a smaller sum
        
        return count
