class Solution:
    def calculate(self, s: str) -> int:
        num=0
        sign='+'
        stack=[]

        for i,char in enumerate(s):
            print(char)
            if char.isnumeric():
                num=10*num+int(char)
            if char in '+/*-' or i==len(s)-1:
                if sign=='+':
                    stack.append(num)
                elif sign=='-':
                    stack.append(-num)
                elif sign=='*':
                    stack.append(stack.pop() * num)
                elif sign=='/':
                    stack.append(math.trunc(stack.pop()/num))
                sign=char
                num=0
        return sum(stack)
