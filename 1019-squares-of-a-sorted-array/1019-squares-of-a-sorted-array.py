class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        res=[]
        while left<=right:
            l=nums[left]*nums[left]
            r=nums[right]*nums[right]
            if l<r:
                res.insert(0,r)
                right-=1
            else:
                res.insert(0,l)
                left+=1
        return res