class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        while left<=right:
            m=left
            self_=True
            while m>0:
                    
                n=m%10
                if n==0 or left%n!=0 :
                    self_=False
                    break
                m=m//10
            if self_:
                res.append(left) 
            left+=1
            
        return res