# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # strictly ascending order
        # 가장 큰 값을 기준으로 계속 나눔

        def divide(l, r) :
            if l > r :
                return
            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = divide(l, mid - 1)
            root.right = divide(mid + 1, r)
            return root

        return divide(0, len(nums) - 1)