class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-num for num in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            val=int(sqrt(-heapq.heappop(gifts)))
            heapq.heappush(gifts,-val)
        return sum(-num for num in gifts)