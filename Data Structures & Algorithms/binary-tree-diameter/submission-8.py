# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = [0]

        def max_diameter(node):
            if not node:
                return 0
            
            l = max_diameter(node.left)
            r = max_diameter(node.right)
            
            max_length[0] = max(max_length[0], l+r)

            return 1 + max(l,r)
        
        max_diameter(root)

        return max_length[0]




        


