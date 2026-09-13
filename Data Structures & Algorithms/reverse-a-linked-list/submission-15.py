# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(curr: None | ListNode, prev: None | ListNode) -> Node | None:
            if curr is None:
                return prev
            
            next = curr.next
            curr.next = prev
            return helper(next, curr)

        return helper(head, None)