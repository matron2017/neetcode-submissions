# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]
        
        def height(root):
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)

            max_diameter[0] = max(l + r, max_diameter[0])

            return max(l,r) + 1
        
        height(root)
        return max_diameter[0]