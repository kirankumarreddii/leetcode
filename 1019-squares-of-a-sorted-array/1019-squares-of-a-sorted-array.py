class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        res=[]
        while left<=right:
            if (nums[left]*nums[left])<(nums[right]*nums[right]):
                res.insert(0,nums[right]*nums[right])
                right-=1
            else:
                res.insert(0,nums[left]*nums[left])
                left+=1
        return res