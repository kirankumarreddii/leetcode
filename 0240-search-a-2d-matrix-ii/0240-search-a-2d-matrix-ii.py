class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=0,len(matrix[0])-1
        while  i<len(matrix) and j>=0:
            if target==matrix[i][j]:
                return True
            elif target<matrix[i][j]:
                j-=1
            else:
                i+=1
        else:
            return False
