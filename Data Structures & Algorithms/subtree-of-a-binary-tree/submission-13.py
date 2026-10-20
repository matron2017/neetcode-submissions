# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (not p and q):
                return False
            
            if p.val != q.val:
                return False

            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        def containsSubtree(node):
            if not node:
                return False

            if isSameTree(node, subRoot):
                return True

            return containsSubtree(node.left) or containsSubtree(node.right)

        return containsSubtree(root)

        


        
        



        