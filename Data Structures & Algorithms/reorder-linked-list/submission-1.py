# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mylen = 0
        curr = head
        while curr:
            mylen+=1
            curr = curr.next

        curr = head
        halfLen = math.ceil(mylen / 2)
        for _ in range(halfLen-1):
            curr = curr.next

        prev = curr
        curr = curr.next
        prev.next = None #disconnect the lists

        prev = None
        while curr: 
            tmp = curr.next
            curr.next = prev
            curr, prev = tmp, curr

        newhead = prev

        curr1, curr2 = head, newhead
        for i in range(mylen-halfLen):
            n1, n2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = n1
            curr1, curr2 = n1, n2

        return
            


