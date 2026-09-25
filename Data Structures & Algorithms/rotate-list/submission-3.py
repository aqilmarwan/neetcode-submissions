# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # [1, 2, 3, 4, 5, 6 ], k = 2 -> [5, 6, 1, 2, 3, 4]

        # (length - k - 1)
        # (6 - 2 - 1) = 3

        # [1 -> 2 -> 3 -> 4 -> NULL -> 5 -> 6]

        if not head:
            return head
        
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        
        newHead = cur.next
        cur.next = None
        tail = newHead.next
        return newHead
            
