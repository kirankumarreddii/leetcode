class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        prime=[2, 3, 5, 7, 11, 13, 17, 19]
        count=0
        while left<=right:
            c=bin(left).count('1')
            if c in prime:
                count+=1
            left+=1
        return count