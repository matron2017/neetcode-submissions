# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSametree(p, q):
            if not p and not q:
                return True

            if (not p and q) or (p and not q):
                return False

            if p.val != q.val:
                return False

            return isSametree(p.left, q.left) and isSametree(p.right, q.right)

        def findSubtree(root):
            if not root:
                return False
            
            if isSametree(root, subRoot):
                return True
            
            return findSubtree(root.left) or findSubtree(root.right)
        
        return findSubtree(root)




        