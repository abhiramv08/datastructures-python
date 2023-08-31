class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if head is None or head.next is None:
                return head
            head_new = head.next
            head_final = self.reverseList(head.next)
            head_new.next = head
            head.next = None
            return head_final
