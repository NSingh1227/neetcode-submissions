# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        checker1 = list1
        checker2 = list2
        while checker1 or checker2:
            if checker1 and checker2:
                if checker1.val <= checker2.val:
                    current.next = checker1
                    current = current.next
                    checker1 = checker1.next
                else:
                    current.next = checker2
                    current = current.next
                    checker2 = checker2.next
            elif checker1:
                current.next = checker1
                current = current.next
                checker1 = checker1.next
            elif checker2:
                current.next = checker2
                current = current.next
                checker2 = checker2.next

        return dummy.next