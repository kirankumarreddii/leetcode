class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat=[[0 for i in range(m)]for j in range(n)]

        def fun(ri,ci):
            for i in range(m):
                mat[ri][i]+=1
            for i in range(n):
                mat[i][ci]+=1

        for ri,ci in indices:
            fun(ri,ci)
        print(mat)
        return sum([1 for row in mat for i in row if i%2!=0])

