class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2=p3=p5=0
        dp=[1]+[0]*(n-1)
        for i in range(1,n):
            next_ugly=min(2*dp[p2],3*dp[p3],5*dp[p5])
            dp[i]=next_ugly
            if next_ugly==3*dp[p3]:
                p3+=1
            if next_ugly==2*dp[p2]:
                p2+=1
            if next_ugly==5*dp[p5]:
    
                p5+=1
        return dp[-1]