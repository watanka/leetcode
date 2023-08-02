# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode()
        tail = answer

        while l1 and l2 :
            if l1.val <= l2.val :
                tail.next = ListNode(l1.val)
                l1 = l1.next
            else :
                tail.next = ListNode(l2.val)
                l2 = l2.next
            tail = tail.next
        # 두 리스트 중 남은 리스트는 answer 뒤에 그대로 붙인다.
        if l1 or l2 :
            tail.next = l1 if l1 else l2
        
        return answer.next
        

        # 2nd.approach
        # if not (l1 or l2) :
        #     return None
        
        # answer = ListNode()
        # tail = answer

        # while l1 or l2 :

        #     if l1 and not l2 :
        #         tail.next = ListNode(l1.val)
        #         l1 = l1.next
        #     elif l2 and not l1 :
        #         tail.next = ListNode(l2.val)
        #         l2 = l2.next

        #     elif l1.val <= l2.val :
        #         tail.next = ListNode(l1.val)
        #         l1 = l1.next
        #     elif l1.val > l2.val :
        #         tail.next = ListNode(l2.val)
        #         l2 = l2.next

        #     tail = tail.next
        # return answer.next
        
        # 1st.approach
        # if not (l1 or l2) :
        #     return None
        # answer = ListNode()
        # tail = answer
    
        # while l1 or l2 :

        #     if not l1 :
        #         tail.val = l2.val
        #         l2 = l2.next
        #     elif not l2 :
        #         tail.val = l1.val
        #         l1 = l1.next
        #     else :
        #         if l1.val <= l2.val :
        #             tail.val = l1.val
        #             l1 = l1.next
        #         elif l1.val > l2.val :
        #             tail.val = l2.val
        #             l2 = l2.next
        #     if l1 or l2 :
        #         tail.next = ListNode()
        #         tail = tail.next
            
        
        
        

        # return answer
