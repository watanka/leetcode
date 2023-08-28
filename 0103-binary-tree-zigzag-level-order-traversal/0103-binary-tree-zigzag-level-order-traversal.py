# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        
        
        # 1st approach. bfs and reverse the subanswer
        if not root :
            return []
        queue = deque([root])
        answer = []

        toward_right = True

        while queue :
            qlen = len(queue)
            subanswer = deque([])
            
            for _ in range(qlen) :
                node = queue.popleft()
                if node :
                    if toward_right :
                        # from left to right    
                        subanswer.append(node.val)
                    else :
                        # from right to left
                        subanswer.appendleft(node.val)


                    if node.left :
                        queue.append(node.left)
                    if node.right :
                        queue.append(node.right)
                    
            
            answer.append(subanswer)
            toward_right = not toward_right

        return answer

                

