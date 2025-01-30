class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def area(x1,y1):
            return x1**2 + y1**2
        heap=[]
        for x,y in points:
            dist=area(x,y)

            if len(heap)<k:
                heapq.heappush(heap,(-dist,[x,y]))
            elif -heap[0][0]>dist:
                heapq.heappop(heap)
                heapq.heappush(heap,(-dist,[x,y]))
        return [point for _,point in heap]
