class Node:
    def __init__(self, val: str):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        curr = self.curr
        curr.next = Node(url)
        curr.next.next = None
        curr.next.prev = curr
        self.curr = curr.next

    def back(self, steps: int) -> str:
        i = 0
        curr = self.curr
        while curr.prev:
            if i == steps:
                break
            curr = curr.prev
            i+= 1
        self.curr = curr
        return curr.val

    def forward(self, steps: int) -> str:
        i = 0
        curr = self.curr
        while curr.next:
            if i == steps:
                break
            curr = curr.next
            i+= 1
        self.curr = curr
        return curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
