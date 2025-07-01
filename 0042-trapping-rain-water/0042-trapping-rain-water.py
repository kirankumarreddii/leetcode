class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        prefix=[0]*len(height)
        sufix=[0]*len(height)
        prefix[0]=height[0]
        sufix[-1]=height[-1]
        for i in range(1,len(height)):
            prefix[i]=max(prefix[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            sufix[i]=max(sufix[i+1],height[i])
        for i in range(len(height)):
            res+=min(prefix[i],sufix[i])-height[i]
        return res
