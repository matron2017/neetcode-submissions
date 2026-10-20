"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #So make hashmap that takes key as the node
        # and ht value is the node with only the val
        # then afterwards create new from head, 
        # and you cna access everyhing withing the val only node
        if head is None: return None
        curr = head
        oldtonew = {}
        while curr:
            new_node = Node(x=curr.val)
            oldtonew[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = oldtonew[curr]
            new_node.next = oldtonew[curr.next] if curr.next else None
            new_node.random = oldtonew[curr.random] if curr.random else None
            curr = curr.next
        return oldtonew[head]

