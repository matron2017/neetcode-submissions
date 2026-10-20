# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = slow.next
        #end of first half (slow)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #now 2 4 8 6
        curr = slow.next  # memorize 6  (from 6->8)
        slow.next = None # cut half, so 2 4 -> none
        prev = None
        while curr:
            temp = curr.next # 8
            curr.next = prev  # 6 -> None    (target is 8 -> 6->none)
            prev = curr # 6 #   now 8 -> 6 -> None
            curr = temp # 8  and now  None
        # head 2 -> 4 -> None
        # prev 8 -> 6 -> None
        
        first, second = head, prev # 4 & 6
        while second:
            tmp1, tmp2 = first.next, second.next # NOne & NOne
            first.next = second #
            second.next = tmp1
            first, second = tmp1, tmp2
            # 2 -> 8 -> 4 -> 6 -> None

        