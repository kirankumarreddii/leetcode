class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        answer=[0]*n
        code=code*2
        if k==0:
            return answer
        window_size=sum(code[1:1+k]) if k>0 else sum(code[n+k:n])
        for i in range(n):
            answer[i]=window_size
            if k>0:
                window_size+=code[i+k+1]-code[i+1]
            else:
                window_size+=code[i+n]-code[i+k+n]
        return answer