"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None}
        curr=head

        while curr: # 1st pass for copying the code
            copy=Node(curr.val)
            oldToCopy[curr]=copy
            curr=curr.next
        curr=head

        while curr:# 2nd pass for setting pointers
            copy=oldToCopy[curr]
            copy.next=oldToCopy[curr.next]
            copy.random=oldToCopy[curr.random]
            curr=curr.next
        return oldToCopy[head]