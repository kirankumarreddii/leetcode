class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x = 1 / x 
            n=-n
        result=1
        cur=x
        while n>0:
            if n%2==1:
                result*=cur
            cur*=cur
            n=n//2
        return result
