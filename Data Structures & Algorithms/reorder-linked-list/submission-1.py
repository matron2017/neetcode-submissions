# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find the end of the first half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # For [2, 4, 6, 8], slow is now at 4
        # 2. Split into two separate lists
        curr = slow.next      # curr points to 6 -> 8
        slow.next = None      # first half is now 2 -> 4 -> None
        # 3. Reverse the second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # first half:  head = 2 -> 4 -> None
        # second half: prev = 8 -> 6 -> None
        # 4. Merge alternating nodes
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        