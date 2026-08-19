# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def _toNum(l):
            curr = l
            s = ""
            while curr:
                s=str(curr.val)+s
                curr=curr.next
            
            return int(s)

        def _toList(n):
            if n == 0: return ListNode(0)
            head = None
            prev = None
            while n:
                node = ListNode(n%10)
                if not head: head = node
                if prev: prev.next = node

                n = n//10
                prev = node
            return head
            
        n1, n2 = _toNum(l1), _toNum(l2)
        print(n1, n2)
        return _toList(n1+n2)

