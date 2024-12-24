class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])

        # def bin(r):
        #     left=0
        #     right=col-1
        #     while left<=right:
        #         mid=(left+right)//2
        #         if matrix[r][mid]==target:
        #             return True
        #         elif matrix[r][mid]<target:
        #             left=mid+1
        #         else:
        #             right=mid-1
        #     return False
        # for i in range(row):
        #         if matrix[i][col-1]>=target:
        #             if bin(i):
        #                 return True
        #             break         
        # return False
        left,right=0,row*col-1
        while left<=right:
            mid=(left+right)//2
            midval=matrix[mid//col][mid%col]
            if midval==target:
                return True
            elif midval<target:
                left=mid+1
            else:
                right=mid-1
        return False
            
