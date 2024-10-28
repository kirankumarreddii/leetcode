class Solution:
    def toLowerCase(self, s: str) -> str:
        st=''
        for l in s:
            if l.isupper():
                st+=l.lower()
            else:
                st+=l
        return st
                

        