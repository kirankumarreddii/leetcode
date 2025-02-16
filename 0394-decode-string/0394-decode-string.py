class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
            else:
                stng=''
                while stack[-1]!='[':
                    stng=stack.pop()+stng
                stack.pop()
                k=''
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k
                stack.append(int(k)*stng)
        return ''.join(stack)