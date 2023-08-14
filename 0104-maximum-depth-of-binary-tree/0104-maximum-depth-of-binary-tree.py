# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        queue = deque([root])
        depth = 0

        while queue :
            for _ in range(len(queue)) :
                node = queue.popleft()
                
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            depth += 1
        return depth
            


        # dfs
        
            

        # 1st approach. consider only depth
        # if not root :
        #     return 0
        # else :
        #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
