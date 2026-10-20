from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# remember edge case
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []

        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue)
            ans.append(queue[-1].val)
            for i in range(n):
                node = queue.popleft()

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return ans

            
            
            
        