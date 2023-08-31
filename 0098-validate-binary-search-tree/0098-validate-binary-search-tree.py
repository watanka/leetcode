# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        isValid = True 
        prev = None

        def inorder(node) :
            nonlocal prev, isValid

            if not node :
                return
            inorder(node.left)
            if prev is not None :
                if node.val <= prev :
                    isValid = False
                    return
            prev = node.val
            inorder(node.right)

        inorder(root)

        return isValid