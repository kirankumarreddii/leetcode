class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip=[[0] *10 for _ in range(10)]

        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[4][6] = skip[6][4] = 5
        skip[2][8] = skip[8][2] = 5
        skip[7][3] = skip[3][7] = 5
        skip[9][1] = skip[1][9] = 5
        skip[6][4] = skip[4][6] = 5
        skip[8][2] = skip[2][8] = 5
        skip[9][7] = skip[7][9] = 8
        skip[3][1] = skip[1][3] = 2
        visited=[False]*10

        def dfs(cur,remaining):
            if remaining==0:
                return 1
            visited[cur]=True
            count=0

            for i in range(1,10):
                if not visited[i] and (skip[cur][i]==0 or visited[skip[cur][i]]):
                    count+=dfs(i,remaining-1)
            visited[cur]=False
            return count

        
        res=0

        for length in range(m,n+1):
            res+=dfs(1,length-1)*4
            res+=dfs(2,length-1)*4
            res+=dfs(5,length-1)
        return res