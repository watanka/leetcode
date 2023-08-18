# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {num : i for i, num in enumerate(inorder)}
        postorder_idx = len(postorder) - 1

        def helper(left, right) :
            nonlocal postorder_idx

            if left > right :
                return 
            
            rootval = postorder[postorder_idx]
            root = TreeNode(rootval)
            postorder_idx -= 1

            root_idx = hashmap[rootval]

            root.right = helper(root_idx + 1, right)
            root.left = helper(left, root_idx - 1)

            return root

        return helper(0, len(postorder) - 1)


        # 1st approach
        # if not inorder or not postorder :
        #     return
        

        # root_val = postorder.pop()
        # root = TreeNode(root_val)
        # root_idx = inorder.index(root_val)

        # root.right = self.buildTree(inorder[root_idx+1: ], postorder)
        # root.left = self.buildTree(inorder[:root_idx], postorder)


        # return root