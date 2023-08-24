# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.inorder(root)
        self.idx = -1

    def next(self) -> int:
        self.idx += 1
        return self.arr[self.idx]
        
    def hasNext(self) -> bool:
        return self.idx < len(self.arr) - 1

    def inorder(self, node) :
        if node : 
            self.inorder(node.left)
            self.arr.append(node.val)
            self.inorder(node.right)
        return node


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()