# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Iteration Version:
        # if head is None:
        #     return None

        # previous_node, current_node = None, head

        # while(current_node):
        #     next_node = current_node.next
        #     current_node.next = previous_node
        #     previous_node = current_node
        #     current_node = next_node

        # return previous_node

        # # Recursive Version:
        return self.reverse_connection(
            previous_node=None,
            head=head,
        )

    def reverse_connection(
        self,
        previous_node: Optional[ListNode],
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        if head is None:
            return None

        next_node = head.next
        head.next = previous_node

        # Base Case
        if next_node is None:
            return head

        # Recursive Call
        return self.reverse_connection(
            previous_node=head,
            head=next_node,
        )

        









