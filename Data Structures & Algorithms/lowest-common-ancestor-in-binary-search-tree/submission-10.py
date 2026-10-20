# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = [root]
        
        def findLCA(node):
            if not node:
                return
                
            lca[0] = node
            if node.val < p.val and node.val < q.val:
                findLCA(node.right)
            elif node.val > p.val and node.val > q.val:
                findLCA(node.left)
            else:
                return
        
        findLCA(root)
        return lca[0]


