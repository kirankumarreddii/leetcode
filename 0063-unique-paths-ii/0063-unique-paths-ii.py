class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1:
            return 0
        dp=[[0]*cols for _ in range(rows)]
        dp[0][0]=1
        for i in range(1,cols):
            if dp[0][i-1]==1 and obstacleGrid[0][i]==0:
                dp[0][i]=1
        for j in range(1,rows):
            if dp[j-1][0]==1 and obstacleGrid[j][0]==0:
                dp[j][0]=1
        for row in range(1,rows):
            for col in range(1,cols):
                if obstacleGrid[row][col]==0:
                    dp[row][col]=dp[row-1][col]+dp[row][col-1]
                else:
                    dp[row][col]=0
        return dp[rows-1][cols-1]