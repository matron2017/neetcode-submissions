# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        slow, fast = first, first.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        prev = None
        while second:    
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev
        #so we want 2->4->None & 8->6->None
        # and we want 2->8->4->6->None
        while first and second:
            tmp1, tmp2 = first.next, second.next # 4, 6
            first.next = second # 2-> 8
            second.next = tmp1 # 2->8->4
            first, second = tmp1, tmp2


