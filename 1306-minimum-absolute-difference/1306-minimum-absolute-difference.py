class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        diff=float('inf')
        arr.sort()
        for i in range(1,len(arr)):
            val=abs(arr[i]-arr[i-1])
            diff=min(diff,val)
        res=[]
        for i in range(1,len(arr)):
            if diff==abs(arr[i]-arr[i-1]):
                res.append([arr[i-1],arr[i]])
        return res