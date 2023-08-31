# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 2nd approach.
        def check(node, low, high):
            if not node: return True
            if  node.val >= high or node.val <= low:
                return False
            return check(node.left, low, node.val) and check(node.right, node.val, high)
        
        return check(root, float('-inf'), float('inf'))

        
        # 1st approach.
        # isValid = True 
        # prev = None

        # def inorder(node) :
        #     nonlocal prev, isValid

        #     if not node :
        #         return
        #     inorder(node.left)
        #     if prev is not None :
        #         if node.val <= prev :
        #             isValid = False
        #             return
        #     prev = node.val
        #     inorder(node.right)

        # inorder(root)

        # return isValid