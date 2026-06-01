# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(
        self, 
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while(len(lists) > 1):
            lists.append(
                self.merge_two_lists(
                    l1=lists.pop(),
                    l2=lists.pop(),
                )
            )
        
        return lists[0]

    def merge_two_lists(
        self,
        l1: ListNode,
        l2: ListNode,
    ) -> ListNode:
        if l1.val < l2.val:
            current_node = l1
            l1 = l1.next
        else:
            current_node = l2
            l2 = l2.next

        head = current_node

        while(l1 and l2):
            if l1.val < l2.val:
                current_node.next = l1
                l1 = l1.next
            else:
                current_node.next = l2
                l2 = l2.next
            current_node = current_node.next

        if l1:
            current_node.next = l1
        elif l2:
            current_node.next = l2

        return head
        


        
        