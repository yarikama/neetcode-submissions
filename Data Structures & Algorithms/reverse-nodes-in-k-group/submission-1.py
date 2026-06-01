# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        cur, cnt = head, 0
        while cur:
            cnt += 1
            cur = cur.next

        return self.reverseK(head, cnt, k)

    def reverseK(self, k_head: Optional[ListNode], cnt: int, k: int) -> Optional[ListNode]:
        if cnt < k:
            return k_head
        
        if not k_head:
            return None

        new_cnt = 0
        prev, curr = None, k_head
        while curr and new_cnt < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            new_cnt += 1

        k_head.next = self.reverseK(curr, cnt - new_cnt, k)

        return prev