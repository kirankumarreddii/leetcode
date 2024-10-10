class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        na=n*(n+1)//2
        lsum=sum(nums)
        setsum=sum(set(nums))
        return[lsum-setsum,na-setsum]