# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False
        
        def dfs(stack, sumval) :
            nonlocal found
            if found or stack[0] is None:
                return
            
            while stack :
                popNode = stack.pop()
                sumval += popNode.val

                if popNode.left :
                    leftstack = stack + [popNode.left]
                    dfs(leftstack, sumval)
                if popNode.right :
                    rightstack = stack + [popNode.right]
                    dfs(rightstack, sumval )
                if not popNode.left and not popNode.right :
                    found = (sumval == targetSum)
                        
                
        dfs(stack = [root], sumval = 0)

        return found



            