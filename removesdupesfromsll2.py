#LC 82: REMOVE DUPLICATES FROM SORTED LINKED LISTS II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0,head)
        cur = head
        prev = dummy
        while cur and cur.next:
            if cur.next.val == cur.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.next
                prev.next = cur
            else:
                prev = cur
                cur = cur.next
        return dummy.next
                
        