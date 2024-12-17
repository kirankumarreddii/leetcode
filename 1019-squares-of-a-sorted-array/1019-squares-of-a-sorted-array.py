class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        res=deque()
        while left<=right:
            l=nums[left]**2
            r=nums[right]**2
            if l<r:
                res.appendleft(r)
                right-=1
            else:
                res.appendleft(l)
                left+=1
        return list(res)