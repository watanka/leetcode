# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
                
        return False



        ## 1st approach. hashmap
        # dic = {}
        # idx = 0
        # if not head : return False

        # while head.next :
        #     if head not in dic.keys() :
        #         dic[head] = 1
        #     else :
        #         return True

        #     head = head.next

        # return False