# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        before = dummy
        while True:
            start = before.next
            if start is None:
                return dummy.next

            stop = start
            for i in range(k):
                if stop is None:
                    return dummy.next
                stop = stop.next
            
            before.next = self.reverse(start, stop)
            before = start


    def reverse(self, start, stop):
        before = stop
        temp = start
        while temp != stop:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return before