# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # remember to check min maxx are correct way
        minn, maxx = float('-inf'), float('inf')

        def validate(node, minn, maxx):
            if not node:
                return True
            
            if node.val >= maxx or node.val <= minn:
                return False

            return validate(node.left, minn, node.val) and validate(node.right, node.val, maxx)

        return validate(root, minn, maxx)