# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def depth(root):
            if not root or not balanced[0]:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)
            
            if abs(l-r) > 1:
                balanced[0] = False

            return max(l, r) + 1

        depth(root)
        return balanced[0]