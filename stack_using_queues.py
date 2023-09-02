#https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:

    def __init__(self):
       self.q1 = []
       self.q2 = [] 

    def push(self, x: int) -> None:
        if len(self.q1) == 0:
            eq = self.q1
            fq = self.q2
        else:
            eq, fq = self.q2, self.q1
        eq.append(x)
        while len(fq) > 0:
            val = fq.pop(0)
            eq.append(val)

    def pop(self) -> int:
        if len(self.q1) == 0: 
            return self.q2.pop(0)
        return self.q1.pop(0)

    def top(self) -> int:
        if len(self.q1) == 0: 
            return self.q2[0]
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0 and len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
