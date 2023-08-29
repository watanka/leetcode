# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import sys

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.minDiff = 1e9
        self.prevNode = None

        def inorder(node) :
            if node is None :
                return

            inorder(node.left)
            if self.prevNode is not None :
                self.minDiff = min(self.minDiff, node.val - self.prevNode)
            self.prevNode = node.val

            inorder(node.right)

        inorder(root)

        return self.minDiff


        # self.minDistance = 1e9
        # # Initially, it will be null.
        # self.prevNode = None

        # def inorder(node):
        #     if node is None:
        #         return
        #     inorder(node.left)
        #     # Find the difference with the previous value if it is there.
        #     if self.prevNode is not None:
        #         self.minDistance = min(self.minDistance, node.val - self.prevNode)
        #     self.prevNode = node.val
        #     inorder(node.right)

        # inorder(root)
        # return self.minDistance


        # # 1st approach. get ordered list and compare neighbors
        # sortList = []
        # minDiff = 10**5
        # lastval = None

        # def sortTree(root) :
        #     if not root :
        #         return

        #     sortTree(root.left)
        #     sortList.append(root)
        #     sortTree(root.right)

        # sortTree(root)
        # for idx in range(len(sortList) - 1) :
        #     prev, nex = sortList[idx], sortList[idx+1]
            
        #     if prev and nex :
        #         minDiff = min(minDiff, abs( prev.val - nex.val ))

        # return minDiff

    




        