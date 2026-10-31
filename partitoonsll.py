#LC 86: PARTITION LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less = ListNode(0)
        greater = ListNode(0)
        l,g = less,greater

        cur = head
        while cur:
            if cur.val<x:
                l.next = cur
                l = l.next
            elif cur.val >= x:
                g.next = cur
                g = g.next
            cur = cur.next
        g.next = None
        l.next = greater.next
        return less.next