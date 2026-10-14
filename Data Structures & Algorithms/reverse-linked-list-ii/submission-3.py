# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        head = ListNode(next=head)
        
        prev, curr = head, head.next
        for _ in range(1, left):
            prev = curr
            curr = curr.next

        left_end = prev
        right_start = curr

        prev = None
        for _ in range(left, right + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        left_end.next = prev
        right_start.next = curr

        return head.next