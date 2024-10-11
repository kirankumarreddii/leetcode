class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        dist=Counter(moves)
        return dist['L']==dist['R'] and dist['U']==dist['D']
        #     return True
        # else:
        #     return False
        