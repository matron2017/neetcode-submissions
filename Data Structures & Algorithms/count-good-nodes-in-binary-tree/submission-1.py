# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        good_nodes = 0
        stk = [(root, float('-inf'))]

        while stk:
            node, largest = stk.pop()

            if node.val >= largest:
                good_nodes += 1

            largest = max(node.val, largest)
            
            if node.right: stk.append((node.right, largest))
            if node.left: stk.append((node.left, largest))

        return good_nodes