# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = tail = dummy
        steps = 0

        while curr and steps < n:
            curr = curr.next
            steps += 1
        while curr.next:
            curr = curr.next
            tail = tail.next
        tail.next = tail.next.next
        return dummy.next