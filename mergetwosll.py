#LC 21: MERGE TWO SORTED LISTS

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        cur = dummy
        cur1 = list1
        cur2 = list2

        while cur1 or cur2:
            val1 = cur1.val if cur1 else float("inf")
            val2 = cur2.val if cur2 else float("inf")

            if val1<=val2 :
                cur.next = ListNode(val1)
                cur = cur.next
                cur1 = cur1.next
            elif val2<=val1:
                cur.next = ListNode(val2)
                cur = cur.next
                cur2 = cur2.next
            
        return dummy.next
