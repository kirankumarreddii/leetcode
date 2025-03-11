class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        l=r=0
        while r<len(s):
            while r<len(s) and s[r]!=' ':
                r+=1
            point=r-1
            while l<point:
                s[l],s[point]=s[point],s[l]
                l+=1
                point-=1
            r+=1
            l=r