# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
            
        length = 0
        curr = head
        while curr :
            curr = curr.next
            length += 1 
        
        if length == 0 :
            return None

        if k % length == 0 :
            return head

        dummy = ListNode(next = head)

        left = head
        right = head

        for _ in range(k % length) :
            right = right.next

        while right.next :
            left = left.next
            right = right.next

        tmp = left.next
        left.next = None
        right.next = head
        

        return tmp