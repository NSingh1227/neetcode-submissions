# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        run1 = l1
        run2 = l2
        carry = 0

        while run1 and run2:
            val = run1.val + run2.val + carry
            if val > 9:
                val %= 10
                carry = 1
            else:
                carry = 0
            new_node = ListNode(val)
            current.next = new_node
            current = current.next
            run1 = run1.next
            run2 = run2.next

        if run1:
            current.next = run1
            while run1:
                val = run1.val + carry
                if val > 9:
                    val %= 10
                    carry = 1
                else:
                    carry = 0
                new_node = ListNode(val)
                current.next = new_node
                current = current.next
                run1 = run1.next
        elif run2:   
            current.next = run2
            while run2:
                val = run2.val + carry
                if val > 9:
                    val %= 10
                    carry = 1
                else:
                    carry = 0
                new_node = ListNode(val)
                current.next = new_node
                current = current.next
                run2 = run2.next
        if (carry > 0):
            new_node = ListNode(carry)
            current.next = new_node
            current = current.next
        
        return dummy.next




