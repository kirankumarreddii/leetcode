class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves)%2==1:
            return False
        dist=Counter(moves)
        if dist['L']==dist['R'] and dist['U']==dist['D']:
            return True
        else:
            return False
        