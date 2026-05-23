# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head

        if not head or not head.next:
            return False

        while fast:

            slow = slow.next

            if not fast.next:
                return False

            fast = fast.next.next

            if fast == slow:
                return True

        return False
            