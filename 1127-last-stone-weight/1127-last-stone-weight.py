class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[]
        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap)!=1:
            max1=-(heapq.heappop(heap))
            max2=-(heapq.heappop(heap))
            heapq.heappush(heap, -abs(max1-max2))
        return -heap[0]
