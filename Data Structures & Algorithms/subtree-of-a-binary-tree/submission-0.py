# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(q, p):
            if q is None and p is None:
                return True
            
            if (q and not p) or (not q and p):
                return False

            if q.val != p.val:
                return False

            return sameTree(q.left, p.left) and sameTree(q.right, p.right)
        
        def has_subTree(root):
            if not root:
                return False

            if sameTree(root, subRoot):
                return True
            
            return has_subTree(root.left) or has_subTree(root.right)
        
        return has_subTree(root)



        