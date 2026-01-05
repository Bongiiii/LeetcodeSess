# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the middle (slow will be at the end of the first half)
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Split and reverse the second half
        midNode = slow.next
        slow.next = None
        
        curr, prevNode = midNode, None
        while curr:
            temp = curr.next
            curr.next = prevNode
            prevNode = curr
            curr = temp

        # Merge the two halves
        first, second = head, prevNode
        
        while second: 
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next