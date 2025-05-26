class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq=dict()
        occur=set()
        for c in s:
            freq[c]=freq.get(c,0)+1
        stack=[]
        for char in s:
            freq[char] -= 1
            if char not in occur:
               
                while stack and ord(char)<=ord(stack[-1]) and freq[stack[-1]]>0:
                    p=stack.pop()
                    occur.remove(p)
                stack.append(char)
                occur.add(char)
                       
        return ''.join(stack)


        