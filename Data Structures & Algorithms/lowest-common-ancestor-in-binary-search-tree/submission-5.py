# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [None]

        def search(root):
            if not root:
                return
        
            lca[0] = root
            if root.val > p.val and root.val > q.val:
                search(root.left)
            elif p.val > root.val and q.val > root.val:
                search(root.right)
            elif root is p or root is q:
                return
            else:
                return

        search(root)
        return lca[0]
        