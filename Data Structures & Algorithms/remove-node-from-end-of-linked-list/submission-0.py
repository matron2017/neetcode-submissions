# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        Dummy = ListNode()  
        Dummy.next = head
        Ahead = Dummy
        Behind = Dummy
        for n in range(n+1):
            Ahead = Ahead.next
        while Ahead:
            Behind = Behind.next
            Ahead = Ahead.next
        Behind.next = Behind.next.next
        
        return Dummy.next
        
        