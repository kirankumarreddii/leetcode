class Solution:
    def canWin(self, currentState: str) -> bool:
        memo={}
        def run_another(state):
            if state in memo:
                return memo[state]
            
            for i in range(len(currentState)-1):
                if state[i]=='+' and state[i+1]=='+':
                    next_s=state[:i]+ '--' + state[i+2:]

                    if not run_another(next_s):
                        memo[state]=True
                        return True
            memo[state]=False
            return False
        return run_another(currentState)