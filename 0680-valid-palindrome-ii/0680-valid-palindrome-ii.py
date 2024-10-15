class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        def check(left,right):
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True
        while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    if check(left+1,right) or check(left,right-1):
                        return True
                    else:
                        return False
        return True
        