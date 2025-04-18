class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val<= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None: 
        if self.min_stack[-1]==self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        

    # def addmin(self,val):
    #     if not self.min_stack:
    #         self.min_stack.append(val)
    #     else:
    #         if self.min_stack[-1]>val:
    #             self.min_stack.append(val)
    #         else:
    #             self.min_stack.append(self.min_stack[-1])
    # def popmin(self):
    #     if not self.min_stack:
    #         return None
    #     else:
    #         self.min_stack.pop()

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()