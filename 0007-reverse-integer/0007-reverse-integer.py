class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX=2**31-1
        INT_MIN=-2**31

        sign=-1 if x<0 else 1

        rev=int(str(abs(x))[::-1])

        rev1=sign*rev
        if rev1 < INT_MIN or rev > INT_MAX:
            return 0
        else:
            return rev1