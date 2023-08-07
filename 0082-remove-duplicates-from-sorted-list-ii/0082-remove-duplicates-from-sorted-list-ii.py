# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None : return head

        dummy = ListNode(next = head)
        prev, curr = dummy, head.next

        while curr :
            # 만약 포인터의 앞 두 값이 같다면
            if prev.next.val == curr.val :
                while curr and prev.next.val == curr.val :
                    curr = curr.next
                prev.next = curr
                if curr :
                    curr = curr.next
            else :
                prev, curr = prev.next, curr.next

        return dummy.next
        
        
        ## 1st.approach
        # dummy = ListNode(next = head)
        # curr = dummy

        # while curr :
        #     if (curr.next and curr.next.next) and curr.next.val == curr.next.next.val :
        #         tmp = curr.next.next
        #         while tmp and tmp.next and tmp.val ==  tmp.next.val :
        #             tmp = tmp.next
        #         curr.next = tmp.next
        #     else :
        #         curr = curr.next
    
        # return dummy.next