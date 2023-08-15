# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        pt = root
        queue = deque([pt])

        while queue :
            for _ in range(len(queue)) :
                node = queue.popleft()
                if node :
                    # if node.left and node.right :
                        # node.left, node.right = node.right, node.left
                    # elif node.left or node.right :
                    node.left, node.right = node.right, node.left
                    queue.append(node.left)
                    queue.append(node.right)
                    
        return root
                
