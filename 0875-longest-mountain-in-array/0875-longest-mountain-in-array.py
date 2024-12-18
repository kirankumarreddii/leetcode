class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res=0
        count=0
        for i in range(1,len(arr)-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                l=i-1
                r=i+1
                count=3
                while l>0 and arr[l]>arr[l-1]:
                    l-=1
                    count+=1
                while  r<len(arr)-1 and arr[r]>arr[r+1]:
                    r+=1
                    count+=1
                res=max(res,r-l+1)
        return res

