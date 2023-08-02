# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not (l1 or l2) :
            return None
        answer = ListNode()
        tail = answer
    
        while l1 or l2 :

            if not l1 :
                tail.val = l2.val
                l2 = l2.next
            elif not l2 :
                tail.val = l1.val
                l1 = l1.next
            else :
                if l1.val <= l2.val :
                    tail.val = l1.val
                    l1 = l1.next
                elif l1.val > l2.val :
                    tail.val = l2.val
                    l2 = l2.next
            if l1 or l2 :
                tail.next = ListNode()
                tail = tail.next
            
        
        
        

        return answer
