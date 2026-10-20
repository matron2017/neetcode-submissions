# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #remember edge cases? what could they be? 
        # that was the latest common error I HAVE MADE
        # Also there is many possible edge cases.
        # most common is if we go through Node = None
        # and we try Node.next -> error !
        Dummy = ListNode()
        curr = Dummy
        carry = 0
        while l1 or l2 or carry > 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val_sum = val1 + val2 + carry
            new_val = val_sum % 10
            carry = val_sum // 10
            curr.next = ListNode(val=new_val)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return Dummy.next
        



