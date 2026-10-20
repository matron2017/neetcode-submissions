# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # remember to check min maxx are correct way
        
        def isValid(node, min_lim, max_lim):
            if not node:
                return True
            
            if node.val <= min_lim or node.val >= max_lim:
                return False
            
            return isValid(node.left, min_lim, node.val) and isValid(node.right, node.val, max_lim)
        
        return isValid(root, float('-inf'), float('inf'))