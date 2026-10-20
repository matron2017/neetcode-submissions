# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]
        def depth(root):
            if not root:
                return 0
            
            l = depth(root.left)
            r = depth(root.right)

            max_diameter[0] = max(l+r, max_diameter[0])

            return max(l, r) + 1
        
        depth(root)
        return max_diameter[0]
        


