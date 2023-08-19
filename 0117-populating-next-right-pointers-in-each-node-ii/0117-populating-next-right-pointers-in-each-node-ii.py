"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        # def helper(root) :
        #     if not root :

        #     root.left.next = helper(root.right

        # 1st. approach
        queue = deque([root])

        while queue :
            
            len_q = len(queue) # initial length of queue is same as # of nodes in same level. connect # nodes-1 that are on same level
            tmp = deque([])
            for i in range(len_q) :

                node = queue.popleft()
                if node :
                    # print(queue[0].val if queue else None)
                    node.next = queue[0] if i < len_q - 1 else None # connect #(samelevel node) - 1
                    if node.left :
                        tmp.append(node.left)
                    if node.right :
                        tmp.append(node.right)
            queue = tmp
        
        
        return root
