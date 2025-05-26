class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq=dict()
        occur=set()
        for c in s:
            if c not in freq:
                freq[c]=0
            freq[c]+=1
        stack=[]
        for char in s:
            freq[char] -= 1
            if char in occur:
                continue
            while stack and ord(char)<ord(stack[-1]) and freq[stack[-1]]>0:
                p=stack.pop()
                occur.remove(p)
            stack.append(char)
            occur.add(char)
                       
        return ''.join(stack)


        