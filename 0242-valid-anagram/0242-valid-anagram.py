class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return counter(s)==counter(t)
    def isAnagram(self, s: str, t: str) -> bool:
        ss=''.join(sorted(s))
        tt=''.join(sorted(t))
        if ss == tt:
            return True
        else:
            return False
    
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
            
        return True