# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_list = None
        for i in range(len(lists) - 1):
            if i == 0:
                merged_list = self.merge2Lists(lists[i], lists[i + 1])
            else:
                merged_list = self.merge2Lists(merged_list, lists[i + 1])
        return merged_list
    
    def merge2Lists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        run1 = list1
        run2 = list2

        while run1 and run2:
            if run1.val <= run2.val:
                current.next = run1
                run1 = run1.next
            else:
                current.next = run2
                run2 = run2.next
            current = current.next

        if run1:
            current.next = run1
        elif run2:
            current.next = run2
        
        return dummy.next
        