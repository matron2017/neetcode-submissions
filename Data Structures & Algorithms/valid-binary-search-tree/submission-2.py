# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minn, maxx = float('-inf'), float('inf')

        def validBST(node, minn, maxx):
            if not node:
                return True

            if node.val >= maxx or node.val <= minn:
                return False

            return validBST(node.left, minn, node.val) and validBST(node.right, node.val, maxx) 
        

        return validBST(root, minn, maxx)