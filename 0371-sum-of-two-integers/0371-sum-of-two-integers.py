class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF 
        INT_MAX=INT_MAX = 0x7FFFFFFF
        while b!=0:
            temp=(a&b)<<1
            a=(a^b)&MASK
            b=temp&MASK
        return a if a<=INT_MAX else ~(a^MASK)
            