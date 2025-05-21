class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        q=[1]
        heapq.heapify(q)
        while n>1:
            num=heapq.heappop(q)
            for p in primes:
                heapq.heappush(q,p*num)
                if num%p==0:
                    break
            n-=1
        return q[0]