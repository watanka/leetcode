# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 노드들의 order가 ascending인지?
        # 중복되는 노드들은 같이 붙어 있는지?
        # 순서는 그대로 유지되어야하는지?

        # input : head
        # dummy pointer
        # pointer의 바로 이전값을 저장하고, 이전값과 지금 가리키고 있는 값이 같다면, 지웁니다.

        # 포인터로 방문
        # 이전값 저장 => prev 포인터도 함께 둡니다.
        # 이전값과 현재값 같다면, 삭제
        # 삭제 로직. prev.next = point.next
        if not head :
            return None
        prev = head
        curr = head
        curr = curr.next

        while curr :
            # 포인터로 방문
            if prev.val == curr.val :
                # 삭제로직
                prev.next = curr.next
            else :
                prev = prev.next
            curr = curr.next

        return head