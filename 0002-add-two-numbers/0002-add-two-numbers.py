# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self) :
        return f'{self.val}'


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 or l2 or carry != 0 :
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            sumval = digit1 + digit2 + carry
            digit = sumval % 10
            carry = sumval // 10

            tail.next = ListNode(digit)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        tail.next = None
        return dummyHead.next