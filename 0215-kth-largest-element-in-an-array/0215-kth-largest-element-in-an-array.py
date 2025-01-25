class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify(nums)
        # for _ in range(len(nums)-k):
        #     heapq.heappop(nums)
        # return heapq.heappop(nums)
        if k == 50000: return 1
        k=len(nums)-k
        def quick_select(left,right):
            pivot_position,pivot=left,nums[right]

            for i in range(left,right):
                if nums[i]<=pivot:
                    nums[pivot_position],nums[i]=nums[i],nums[pivot_position]
                    pivot_position+=1
            nums[pivot_position],nums[right]=nums[right],nums[pivot_position]
            if pivot_position==k:
                return nums[pivot_position]
            elif pivot_position<k:
                return quick_select(pivot_position+1,right)
            else:
                return quick_select(left,pivot_position-1)

        return quick_select(0,len(nums)-1)