# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        cnt = 0

        def bfs(queue) :
            nonlocal cnt
            while queue :
                node = queue.popleft() 
                
                if node :
                    cnt += 1
                    if node.left :
                        queue.append(node.left)
                    if node.right :
                        queue.append(node.right)

        bfs(deque([root]))

        return cnt