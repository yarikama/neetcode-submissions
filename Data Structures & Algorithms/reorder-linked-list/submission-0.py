# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 1. use fast slow pointer to get the medium
# 2. reverse the second part
    # [**IMPORTANT**] 
    # CAN'T INIT LIKE THIS
    #   prev = slow
    #   cur = slow.next
# 3. connect from reverse head and head: 1 -> n-1 -> 2 ...

# Edge Case
# 2 4 6 8
# 2 4 6 (original)
# 8 6 (reverse)
# stop when reverse_cur.next is None 



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find medium
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the secod part
        prev = None
        cur = slow

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        cur = head
        reverse_cur = prev
        while cur and reverse_cur and reverse_cur.next: 
            next = cur.next
            r_next = reverse_cur.next

            cur.next = reverse_cur  # 1 -> n-1
            reverse_cur.next = next # n-1 -> 2
            
            cur = next
            reverse_cur = r_next


            
             


        
            



        