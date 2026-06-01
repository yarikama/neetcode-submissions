# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# ________N___


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        for _ in range(n):
            cur = cur.next

        prev, to_remove = None, head
        while cur:
            cur = cur.next
            prev = to_remove
            to_remove = to_remove.next

        if not prev:
            return None

        prev.next = to_remove.next

        return head
