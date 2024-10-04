class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res=[]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res.append(mat[i][j])
        t=[]
        inx=0
        if len(res) != r * c:
            return mat 
        for i in range(r):
            tem=[]
            for j in range(c):
                tem.append(res[inx])
                inx+=1
            t.append(tem)
        return t