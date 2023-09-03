"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node :
            return

        queue = collections.deque([node])
        clones = {node.val : Node(node.val, [])}

        while queue :
            cur = queue.popleft()
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors :
                if ngbr.val not in clones :
                    clones[ngbr.val] = Node(ngbr.val, [])
                    queue.append(ngbr)

                cur_clone.neighbors.append(clones[ngbr.val])
            
        return clones[node.val]
                    
