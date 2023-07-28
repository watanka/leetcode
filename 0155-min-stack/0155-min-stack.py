class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack :
            # if self.minStack[-1] > val :
            #     self.minStack.append(val)
            # else :
            #     minval = min(val, self.minStack[-1]) # record the minimum value at the time
            #     self.minStack.append(minval)

            self.minStack.append(min(val, self.minStack[-1]))
            
        else :
            self.minStack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


    ## 2nd approach. use minValue
    # def __init__(self):
    #     self.stack = []
    #     self.minValue = 2**31 - 1

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if self.minValue > val :
    #         self.minValue = val

    # def pop(self) -> None:

    #     popVal = self.stack.pop(-1)
    #     if self.minValue == popVal :
    #         if self.stack :
    #             self.minValue = min(self.stack)
    #         else :
    #             self.minValue = 2**31 - 1
        

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.minValue


    ## 1st approach. use list
    # def __init__(self):
    #     self.stack = []
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)

    # def pop(self) -> None:
    #     self.stack.pop(-1)

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()