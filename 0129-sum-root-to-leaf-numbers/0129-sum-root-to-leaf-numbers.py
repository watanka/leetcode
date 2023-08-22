# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ## 2nd. recursive
        result = 0
        def helper(node, r_to_l_sum) :
            nonlocal result
            if not node :
                return
            if not node.left and not node.right :
                # convert root to left path into a number
                root2left_sum = int(''.join(map(str, r_to_l_sum + [node.val])))
                result += root2left_sum
            helper(node.left, r_to_l_sum + [node.val])
            helper(node.right, r_to_l_sum + [node.val])

        helper(root, [])
        return result

        ## 1st. approach dfs
        # def dfs(stack, root_leaf_path) :
        #     nonlocal result
        #     while stack :
        #         node = stack.pop()
        #         root_leaf_path.append(node.val)

        #         if not node.left and not node.right :
        #             root_leaf_sum = int(''.join(map(str, root_leaf_path)))
        #             result += root_leaf_sum
        #             return

        #         if node.left :
        #             dfs(stack + [node.left], root_leaf_path)
        #             root_leaf_path.pop()
        #         if node.right :
        #             dfs(stack + [node.right], root_leaf_path)
        #             root_leaf_path.pop()
                
                
        
        # result = 0        
        # stack = [root]
        # dfs(stack, root_leaf_path = [])

        # return result
                


