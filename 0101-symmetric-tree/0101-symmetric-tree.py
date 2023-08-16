# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        def helper(lnode, rnode) :
            if not lnode and not rnode :
                return True
            if not lnode or not rnode :
                return False
            if lnode.val != rnode.val :
                return False
            return helper(lnode.left, rnode.right) and helper(lnode.right, rnode.left)
                


        return helper(root.left, root.right)