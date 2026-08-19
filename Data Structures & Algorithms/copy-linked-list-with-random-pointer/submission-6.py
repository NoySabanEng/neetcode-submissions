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
        while curr:
            n = Node(curr.val)
            nodeMap[curr] = n
            curr = curr.next

        curr = head
        while curr:
            ncurr = nodeMap[curr]
            ncurr.next = nodeMap[curr.next] if curr.next else None
            ncurr.random = nodeMap[curr.random] if curr.random else None
            curr = curr.next

        return nodeMap[head]



        