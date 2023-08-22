# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(stack, root_leaf_path) :
            nonlocal result
            while stack :
                node = stack.pop()
                
                if not node.left and not node.right :
                    root_leaf_sum = int(''.join(map(str,root_leaf_path + [node.val])))
                    result += root_leaf_sum
                    return

                if node.left :
                    dfs(stack + [node.left], root_leaf_path + [node.val])
                if node.right :
                    dfs(stack + [node.right], root_leaf_path + [node.val])
                
                
        
        result = 0        
        stack = [root]
        dfs(stack, root_leaf_path = [])

        return result
                


