class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        def call(key):
            left=0
            right=len(nums)-1
            li=0
            while nums[left]!=key:
                left+=1
            while nums[right]!=key:
                right-=1
            return right-left+1     
        dist={}
        for n in nums:
            if n not in dist:
                dist[n]=1
            else:
                dist[n]+=1
        degree = max(dist.values())
        length=float('inf')
        for key,val in dist.items():
            if val==degree:
                fun=call(key)
                length=min(fun,length)
        return length