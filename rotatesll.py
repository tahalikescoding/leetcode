#LC 61: ROTATE LINKED LIST 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n+=1
        k = k%n
        if not k:
            return head

        tail.next = head
        new_tail = head
        for _ in range(n-k-1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head 

        


        