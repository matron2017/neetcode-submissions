# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head 
        if current is None:
            return None
        past_next = current.next 
        past_current = current 
        current.next = None  

        while past_next != None:
            current = past_next 
            past_next = current.next 
            current.next = past_current   
            past_current = current    

        return current
        

