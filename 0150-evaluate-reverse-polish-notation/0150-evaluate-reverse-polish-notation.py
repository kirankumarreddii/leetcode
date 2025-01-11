class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # stack=[int(tokens[0])]
        # i=1
        # while stack:
        #     if i<len(tokens):
        #         if tokens[i] not in ["+", "-", "*", "/"]:
        #             stack.append(int(tokens[i]))
        #             i+=1
        #         else:
        #             right=stack.pop()
        #             left=stack.pop()
        #             if tokens[i] == "+":
        #                 stack.append(left + right)
        #             elif tokens[i] == "-":
        #                 stack.append(left - right)
        #             elif tokens[i] == "*":
        #                 stack.append(left * right)
        #             elif tokens[i] == "/":
        #                 stack.append(int(left / right))
        #             i+=1
        #     else:
        #         break
        # return stack[0]
        stack=[]
        for token in  tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                right=stack.pop()
                left=stack.pop()
                if token == "+":
                    stack.append(left + right)
                elif token == "-":
                    stack.append(left - right)
                elif token == "*":
                    stack.append(left * right)
                elif token == "/":
                    stack.append(int(left / right))
        return stack[0]