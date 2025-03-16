class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if (len(matrix)==len(matrix[0])):
            for i in range(len(matrix)):
                for j in range(i,len(matrix)):
                    if i!=j:
                        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            return matrix
        else:
            temp=[[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return temp     