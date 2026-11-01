#LC 148: SORT LINKED LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getmid(self,head):
        slow , fast = head , head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self,left,right):
        dummy = ListNode(0)
        cur = dummy
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next 
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        elif right:
            cur.next = right
        return dummy.next
        
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        left = head
        right = self.getmid(head)
        tmp = right.next
        right.next = None
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left,right)
        