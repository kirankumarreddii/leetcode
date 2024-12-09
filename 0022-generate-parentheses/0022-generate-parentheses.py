class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def track(current,open,close):
            if len(current)==2*n:
                res.append(current)
                return 
            if open<n:
                track(current+'(',open+1,close)
            if close<open:
                track(current+')',open,close+1)



        track('',0,0)
        return res