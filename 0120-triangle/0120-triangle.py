class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for rows in range(len(triangle)-2,-1,-1):
            for cols in range(len(triangle[rows])):
                triangle[rows][cols]+=min(triangle[rows+1][cols],triangle[rows+1][cols+1])
        return triangle[0][0]
        