class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n==0:
            return 0
        if n==1:
            return k
        same=k*1
        different=k*(k-1)
        total=different+same
        for i in range(3,n+1):
            same=different
            different=total*(k-1)
            total=different+same
        return total

        