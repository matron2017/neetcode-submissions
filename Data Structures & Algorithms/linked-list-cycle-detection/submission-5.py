# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Dummy = ListNode()
        Dummy.next = head
        Ahead = Dummy
        Behind = Dummy
        while Ahead and Ahead.next:
            Ahead = Ahead.next.next
            Behind = Behind.next
            if Ahead == Behind:
                return True

        return False


    