# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # 2nd. recursive
        if not root :
            return None
        def recursive(node) :
            if node :
                node.left, node.right = node.right, node.left
                recursive(node.left)
                recursive(node.right)
            return node

        return recursive(root)

        # # 1st bfs
        # pt = root
        # queue = deque([pt])

        # while queue :
        #     for _ in range(len(queue)) :
        #         node = queue.popleft()
        #         if node :
        #             node.left, node.right = node.right, node.left
        #             queue.append(node.left)
        #             queue.append(node.right)
                    
        # return root
                
