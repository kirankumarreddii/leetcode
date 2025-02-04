class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binarysearch(res,num):
            l,r=0,len(res)-1
            while l<=r:
                mid=(l+r)//2
                if res[mid]<num:
                    l=mid+1
                else:
                    r=mid-1
            return l

        res=[]
        for num in nums:
            l=0
            r=len(res)-1
            if len(res)==0 or res[-1]<num:
                res.append(num)
            else:
                pos=binarysearch(res,num)
                res[pos]=num
        return len(res)
        