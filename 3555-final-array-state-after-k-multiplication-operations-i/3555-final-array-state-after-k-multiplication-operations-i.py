class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if not nums or k == 0 or multiplier == 1:
            return nums
        heap=[(num,i) for i,num in enumerate(nums)]
        heapq.heapify(heap)
        
        for _ in range(k):
            val,idx=heapq.heappop(heap)
            nums[idx]=val*multiplier
            heapq.heappush(heap,(nums[idx],idx))
        
        return nums