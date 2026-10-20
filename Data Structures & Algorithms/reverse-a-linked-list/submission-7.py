# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_next = None
        while current != None:
            old_next = current.next
            current.next = new_next
            new_next = current
            current = old_next

        return new_next
