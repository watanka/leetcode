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

        sortList = []
        minDiff = 10**5

        def sortTree(root) :
            if not root :
                return

            sortTree(root.left)
            sortList.append(root)
            sortTree(root.right)

        sortTree(root)
        for idx in range(len(sortList) - 1) :
            prev, nex = sortList[idx], sortList[idx+1]
            
            if prev and nex :
                minDiff = min(minDiff, abs( prev.val - nex.val ))

        return minDiff

    




        