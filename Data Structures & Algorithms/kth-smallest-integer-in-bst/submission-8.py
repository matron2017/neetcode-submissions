# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #remember the basic syntax:
        # always check the node name vairalbe name
        # inner fucntion variable name and global class names
        # so no mixing them accidentally.
        kth = [0]
        count = [k]
        def search(node):
            if not node:
                return
            
            search(node.left)      

            if count[0] == 1:
                kth[0] = node.val

            count[0] = count[0] - 1
            if count[0] > 0:
                search(node.right)
                
        search(root)
        return kth[0]

