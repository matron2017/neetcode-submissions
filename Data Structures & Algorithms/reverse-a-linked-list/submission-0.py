# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
         #      [1 ->2->3]  so head is 1, next is 2
        current = head # 1
        if current == None:
            return current
        past_next = current.next # 2
        past_current = current # 1
        current.next = None  #  so now  None<-1, 2->3->None

        while past_next != None:
            current = past_next 
            past_next = current.next 
            current.next = past_current   
            past_current = current    
        return current
        

