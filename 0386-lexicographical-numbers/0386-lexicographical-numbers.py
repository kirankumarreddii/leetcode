class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def next_number(current,n):
            if current*10<=n:
                return current*10
            
            if current>=n:
                current//=10
            current+=1

            while current%10==0:
                current//=10

            return current
        res=[]
        current=1

        for _ in range(n):
            res.append(current)
            current=next_number(current,n)

        return res
        