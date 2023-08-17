# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def __init__(self) :
        self.preorder_index = 0
        self.preorder = None

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        hashmap = {num : i for i, num in enumerate(inorder)}
        self.preorder = preorder

        def _buildTree(left, right) :
            if left > right :
                return

            rootval = self.preorder[self.preorder_index]
            root = TreeNode(rootval)

            self.preorder_index += 1        

            next_right = hashmap[rootval]
            root.left = _buildTree(left, next_right - 1)
            root.right = _buildTree(next_right + 1, right)

            return root
        
        return _buildTree(0, len(inorder) - 1)
