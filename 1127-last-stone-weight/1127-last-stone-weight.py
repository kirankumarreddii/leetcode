class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones)!=1:
            max1=-(heapq.heappop(stones))
            max2=-(heapq.heappop(stones))
            heapq.heappush(stones, -abs(max1-max2))
        return -stones[0]
