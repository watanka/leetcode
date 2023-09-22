# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        dummy = answer

        while l1 or l2 :
            if not l1 and l2 :
                dummy.next = l2
                l2 = None
            elif not l2 and l1 :
                dummy.next = l1
                l1 = None
            elif l1 and l2 :      
                if l1.val >= l2.val :
                    dummy.next = ListNode(val = l2.val)
                    l2 = l2.next
                else :
                    dummy.next = ListNode(val = l1.val)
                    l1 = l1.next
                dummy = dummy.next

        return answer.next