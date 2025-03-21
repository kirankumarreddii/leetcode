class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def build(num):
            if num==0:
                return ['']
            elif num==1:
                return ['0','1','8']
            temp=build(num-2)
            res=[]
            for let in temp:
                if num!=n:
                    res.append('0'+let+'0')
                res.append('1'+let+'1')
                res.append('6'+let+'9')
                res.append('8'+let+'8')
                res.append('9'+let+'6')
            return res


        return build(n)