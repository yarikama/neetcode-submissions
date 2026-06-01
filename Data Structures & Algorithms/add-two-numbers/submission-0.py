# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = self._get_sum(l1)
        sum2 = self._get_sum(l2)
        return self._get_linked_list(sum1+sum2)

        
    def _get_sum(self, node: Optional[ListNode]) -> int:
        sum = 0
        acc = 1
        while node:
            sum += node.val * acc
            acc *= 10
            node = node.next
        return sum

    def _get_linked_list(self, num) -> Optinoal[ListNode]:
        if num == 0:
            return None

        root = ListNode(num%10)
        num //= 10

        prev = root
        while num > 0:
            prev.next = ListNode(num%10)
            prev = prev.next
            num //= 10

        return root
            

