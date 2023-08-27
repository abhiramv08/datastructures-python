class MinStack:

    stack: List = None
    n: int = None

    def __init__(self):
        self.stack = []
        self.n = -1

    def push(self, val: int) -> None:
        if(self.n == -1):
            self.stack.append((val, val))
        else:
            top, topMin = self.stack[self.n]
            if(val < topMin):
                self.stack.append((val, val))
            else:
                self.stack.append((val, topMin))
        self.n+= 1

    def pop(self) -> None:
        self.stack.pop()
        self.n-= 1
        

    def top(self) -> int:
        top= self.stack[self.n][0]
        return top

    def getMin(self) -> int:
        topMin = self.stack[self.n][1]
        return topMin
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
