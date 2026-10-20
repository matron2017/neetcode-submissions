# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]
        def height(root):
            if root is None or not balanced[0]:
                return 0
            
            l = height(root.left)
            r = height(root.right)

            if abs(l-r) > 1:
                balanced[0] = False
            
            return max(l,r) + 1
        
        height(root)
        return balanced[0]