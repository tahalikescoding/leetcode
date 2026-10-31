#LC 92: REVERSE LINKED LIST CYCLE II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        count = 1
        dummy = ListNode(0,head)
        cur = head
        start = dummy
        while count != left and cur:
            start = cur
            cur = cur.next
            count+=1
        lefthead = cur
        prev = cur
        cur = cur.next
        count+=1
        while cur and count<=right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt 
            count+=1
        start.next = prev
        lefthead.next = cur
        return dummy.next