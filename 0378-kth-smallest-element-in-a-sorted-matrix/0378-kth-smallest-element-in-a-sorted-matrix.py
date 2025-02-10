class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        def county(matrix,mid):
            count,row,col=0,n-1,0
            while row>=0 and col<n:
                if matrix[row][col]<=mid:
                    count+=row+1
                    col+=1
                else:
                    row-=1
            return count
        low,high=matrix[0][0],matrix[-1][-1]
        while low<high:
            mid=(low+high)//2
            if county(matrix,mid)<k:
                low=mid+1
            else:
                high=mid
        return low
