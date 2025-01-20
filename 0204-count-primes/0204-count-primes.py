class Solution:
    def countPrimes(self, n: int) -> int:
    
        if n < 3:
            return 0
        
        # Step 1: Initialize prime list
        prime = [False, False] + [True] * (n - 2)  # 0 and 1 are not prime

        # Step 2: Apply Sieve of Eratosthenes
        for i in range(2, int(n**0.5) + 1):  # Check only up to sqrt(n)
            if prime[i]:  # If i is prime
                j = i * i  # Start marking multiples from i^2
                while j < n:
                    prime[j] = False  # Mark as non-prime
                    j += i  # Move to next multiple of i
        
        # Step 3: Return count of primes
        return sum(prime)