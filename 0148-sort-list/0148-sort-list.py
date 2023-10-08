# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head -> val -> head.next

        # naive approach. save all the value and return list

        dummy = head    
        ls = []
        while dummy :
            ls.append(dummy.val)
            dummy = dummy.next

        ls.sort()

        newNode = ListNode()
        pt = newNode
        for ele in ls :
            pt.next = ListNode(val = ele)
            pt = pt.next

        return newNode.next