class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]
        for op in operations:
            if op=='C':
                res.pop()    
            elif op=='D':
                res.append(2*res[-1])
                print(res)
            elif op=='+':
                res.append(res[-2]+res[-1])    
            else:
                res.append(int(op))
        return sum(res)
        