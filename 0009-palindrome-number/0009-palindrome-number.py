class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if str(x)[::-1]==str(x):
            return True
        else:
            return False