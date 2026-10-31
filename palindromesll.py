#LC 234: PALINDORME LINKED LIST

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        #Find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Rverse everything after muddle
        prev = None
        cur = slow 
        while cur:
            nxt = cur.next 
            cur.next = prev 
            prev = cur
            cur = nxt 
        
        #compare
        right = prev
        left = head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True