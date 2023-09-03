#https://leetcode.com/problems/merge-k-sorted-lists/submissions/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #Bad execution - O(n^2)
        j = 0
        n = len(lists)
        while j < n:
            if lists[j] is None:
                lists.pop(j)
                j-= 1
                n-= 1
            j+= 1
        merged = None
        tail = None
        while n > 0:
            i, mVal, mIndex = 0,0,0
            mVal = lists[0].val
            while i < n:
                if lists[i].val < mVal:
                    mVal, mIndex = lists[i].val, i
                i+=1
            if merged is None:
                merged = ListNode(mVal, None)
                tail = merged
            else:
                tail.next = ListNode(mVal, None)
                tail = tail.next
            lists[mIndex] = lists[mIndex].next
            if lists[mIndex] is None:
                lists.pop(mIndex)
                n-= 1
        return merged
