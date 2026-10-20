# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None

        stk = [(root, float('-inf'))]

        good_nodes = 0
        while stk:
            node, max_val = stk.pop()

            # current node is larger than any node from root until this node
            if node.val >= max_val:
                good_nodes += 1
                max_val = node.val
            
            if node.right: stk.append((node.right, max_val))
            if node.left: stk.append((node.left, max_val))
        
        return good_nodes


            

