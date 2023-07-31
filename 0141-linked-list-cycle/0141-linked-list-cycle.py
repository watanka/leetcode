# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        dic = {}
        idx = 0
        if not head : return False
        
        while True :
            if not head.next :
                return False
            elif head not in dic.keys() :
                dic[head] = 1
            else :
                return True

            head = head.next

        return False