class Solution:
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        prime=[False,False]+[True]*(n-2)

        for i in range(2,int(n**0.5) + 1):
            if prime[i]:
                j=i*i
                while j<n:
                    prime[j]=False
                    j+=i
        return sum(prime)
