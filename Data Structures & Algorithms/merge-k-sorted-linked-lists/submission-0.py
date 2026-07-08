# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        if all(node is None for node in lists):
            return None

        dummy = ListNode(0)
        trail = dummy

        currs = lists[:]

        while any(curr is not None for curr in currs):
            min_index = -1
            min_value = float("inf")

            for i in range(len(currs)):
                if currs[i] is not None and currs[i].val < min_value:
                    min_value = currs[i].val
                    min_index = i
            trail.next = currs[min_index]
            trail = trail.next

            currs[min_index] = currs[min_index].next
        return dummy.next