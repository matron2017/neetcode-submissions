# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # remember to check min maxx are correct way
        
        def validTree(node, min_lim, max_lim):
            if not node:
                return True
            
            if node.val <= min_lim or node.val >= max_lim:
                return False
            
            return validTree(node.left, min_lim, node.val) and validTree(node.right,   node.val, max_lim)
        
        return validTree(root, float('-inf'), float('inf'))