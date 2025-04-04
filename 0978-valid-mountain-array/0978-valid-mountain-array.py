class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        i=0
        l=j=len(arr)-1
        while i+1<l+1 and arr[i]<arr[i+1]:
            i+=1
        while j-1>=0 and arr[j-1]>arr[j]:
            j-=1
        return i == j and i != 0 and i != l