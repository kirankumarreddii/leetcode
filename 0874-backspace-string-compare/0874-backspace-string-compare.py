class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(a):
            stack=[]
            for i in a:
                if i!= '#':
                    stack.append(i)
                else:
                    if stack: 
                        stack.pop()

            return ''.join(stack)

        return process(s)==process(t)