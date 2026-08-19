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
        if not head: return None
        nodeMap = {}

        curr = head
        prevn = None
        while curr:
            n = Node(curr.val)
            nodeMap[curr] = n
            if prevn: prevn.next = n
            prevn = n
            curr = curr.next

        curr = head
        ncurr = nodeMap[head]
        while curr:
            nrand = nodeMap[curr.random] if curr.random else None
            ncurr.random = nrand
            curr = curr.next
            ncurr = ncurr.next

        return nodeMap[head]



        