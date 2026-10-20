# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def SameTree(p, q):
            if not p and not q:
                return True

            if (p and not q) or (not p and q):
                return False

            if p.val != q.val:
                return False
            
            return SameTree(p.left, q.left) and SameTree(p.right, q.right)

        def SubTree(root):
            if not root:
                return False
            
            if SameTree(root, subRoot):
                return True

            return SubTree(root.left) or SubTree(root.right)
        
        return SubTree(root)




        