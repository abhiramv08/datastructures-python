class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next  

class MyLinkedList:

    def __init__(self):
        self.head = None      

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        if index < 0:
            return -1
        while curr:
            if index == i:
                return curr.val
            curr = curr.next
            i+= 1
        return -1

    def addAtHead(self, val: int) -> None:
        #curr = MyLinkedList()
        #curr.val = val
        if self.head is None:
            self.head = Node(val, None)
            return
        temp = self.head
        self.head = Node(val, temp)

    def addAtTail(self, val: int) -> None:
        curr = self.head
        if self.head is None:
            self.head = Node(val, None)
            return
        while curr.next:
            curr = curr.next
        curr.next = Node(val, None)

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        i = 0
        if index == 0:
            return self.addAtHead(val)
        while curr:
            if i == (index-1):
                temp = curr.next
                curr.next = MyLinkedList()
                curr.next.val = val
                curr.next.next = temp
                return
            curr = curr.next
            i+= 1

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i = 0
        if index == 0:
            self.head = self.head.next
        while curr.next:
            if i == (index-1):
                curr.next = curr.next.next
                return
            curr = curr.next   
            i+= 1     


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
