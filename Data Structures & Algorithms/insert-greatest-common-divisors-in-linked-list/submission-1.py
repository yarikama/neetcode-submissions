# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a%b
            return a

        curr = head
        while curr and curr.next:
            new_node = ListNode(gcd(curr.val, curr.next.val), curr.next)
            curr.next = new_node
            curr = new_node.next

        return head


