# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        first  = head
        Dummy  = ListNode()
        second = Dummy

        second.next = head

        for i in range(n):
            first = first.next

        while first:

            first  = first.next
            second = second.next

        temp = second.next
        second.next = second.next.next
        temp.next = None

        return Dummy.next




