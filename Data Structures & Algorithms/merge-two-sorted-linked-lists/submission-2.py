# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2

        if not list2:
            return list1

        if list1.val < list2.val:
            cur1, cur2 = list1, list2
        else:
            cur2, cur1 = list1, list2

        head = cur1

        while cur1 and cur2:
            if cur1.next and cur1.next.val < cur2.val:
                cur1 = cur1.next
            else:
                next = cur1.next
                cur1.next = cur2
                cur1 = cur2
                cur2 = next

        return head

                
                

        