# # class Solution:
# #     def wiggleSort(self, nums: List[int]) -> None:
# #         """
# #         Do not return anything, modify nums in-place instead.
# #         """
# #         for i in range(len(nums)-1):
# #             if ((i%2==0 and nums[i]>nums[i+1])  or (i%2==1 and nums[i]<nums[i+1])):
# #                 nums[i],nums[i+1]=nums[i+1],nums[i]
        


# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         # for i in range(len(nums) - 1):
#         #     if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
#         #         nums[i], nums[i + 1] = nums[i + 1], nums[i]

#         n=len(nums)
#         def partition(nums,left,right,pivot_index):
#             nums[pivot_index],nums[right]=nums[right],nums[pivot_index]
#             pivot=nums[right]
#             store=left
#             for i in range(left,right):
#                 if nums[i]<pivot:
#                     nums[i],nums[store]=nums[store],nums[i]
#                     store+=1
            
#             nums[store],nums[right]=nums[right],nums[store]
#             return store
                

#         def quickselect(nums, left, right, k):
#             if left == right:
#                 return nums[left]
            
#             pivot_index = random.randint(left, right)
#             partition_index=partition(nums,left,right,pivot_index)
#             if partition_index == k:
#                 return nums[k]
#             elif partition_index < k:
#                 return quickselect(nums, partition_index + 1, right, k)
#             else:
#                 return quickselect(nums, left, partition_index - 1, k)
#         # partition(nums,0,n,n//2)
#         median = quickselect(nums, 0, n-1, n // 2)

#         def index(i):
#             return (2 * i + 1) % (n| 1)

#         left,mid,right=0,0,n-1
#         while left<=right:
#             if nums[index(mid)]>median:
#                 nums[index(left)],nums[index(mid)]=nums[index(mid)],nums[index(left)]
#                 left+=1
#                 mid+=1
#             elif nums[index(mid)]<median:
#                 nums[index(right)],nums[index(mid)]=nums[index(mid)],nums[index(right)]
#                 right-=1
#             else:
#                 mid+=1

# from typing import List
# import random

# class Solution:
#     def wiggleSort(self, nums: List[int]) -> None:
#         n = len(nums)

#         # Partition function for QuickSelect
#         def partition(nums, left, right, pivot_index):
#             pivot_value = nums[pivot_index]
#             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # Move pivot to end
#             store_index = left
#             for i in range(left, right):
#                 if nums[i] < pivot_value:
#                     nums[i], nums[store_index] = nums[store_index], nums[i]
#                     store_index += 1
#             nums[store_index], nums[right] = nums[right], nums[store_index]  # Move pivot to final place
#             return store_index

#         # QuickSelect function to find the median
#         def quickselect(nums, left, right, k):
#             if left == right:
#                 return nums[left]
#             pivot_index = random.randint(left, right)
#             pivot_index = partition(nums, left, right, pivot_index)

#             if k == pivot_index:
#                 return nums[k]
#             elif k < pivot_index:
#                 return quickselect(nums, left, pivot_index - 1, k)
#             else:
#                 return quickselect(nums, pivot_index + 1, right, k)

#         # Find median using QuickSelect
#         median = quickselect(nums, 0, n - 1, n // 2)

#         # Index-mapping function
#         def index(i):
#             return (2 * i + 1) % (n | 1)

#         # 3-way partitioning around the median
#         left, mid, right = 0, 0, n - 1
#         while mid <= right:
#             if nums[index(mid)] > median:
#                 nums[index(left)], nums[index(mid)] = nums[index(mid)], nums[index(left)]
#                 left += 1
#                 mid += 1
#             elif nums[index(mid)] < median:
#                 nums[index(right)], nums[index(mid)] = nums[index(mid)], nums[index(right)]
#                 right -= 1
#             else:
#                 mid += 1
from typing import List
import random

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)

        # Partition function for QuickSelect
        def partition(nums, left, right, pivot_index):
            pivot_value = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]  # Move pivot to end
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot_value:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            nums[store_index], nums[right] = nums[right], nums[store_index]  # Move pivot to final place
            return store_index

        # QuickSelect function to find the median
        def quickselect(nums, left, right, k):
            if left == right:
                return nums[left]

            pivot_index = random.randint(left, right)
            pivot_index = partition(nums, left, right, pivot_index)

            if k == pivot_index:
                return nums[k]
            elif k < pivot_index:
                return quickselect(nums, left, pivot_index - 1, k)
            else:
                return quickselect(nums, pivot_index + 1, right, k)

        # Step 1: Find the median
        median = quickselect(nums, 0, n - 1, n // 2)

        # Step 2: Define Index Mapping
        def index(i):
            return (2 * i + 1) % (n | 1)

        # Step 3: Three-way partitioning
        left, mid, right = 0, 0, n - 1
        while mid <= right:
            if nums[index(mid)] > median:
                nums[index(left)], nums[index(mid)] = nums[index(mid)], nums[index(left)]
                left += 1
                mid += 1
            elif nums[index(mid)] < median:
                nums[index(right)], nums[index(mid)] = nums[index(mid)], nums[index(right)]
                right -= 1
            else:
                mid += 1
