# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = [k]
        kth_smallest = [0]

        def search(node):
            if not node:
                return

            search(node.left)

            if kth[0] == 1:
                kth_smallest[0] = node.val

            kth[0] = kth[0]-1

            if kth[0] > 0:
                search(node.right) 
        
        search(root)
        return kth_smallest[0]
        
