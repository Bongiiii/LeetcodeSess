# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(next=head)
        curr = temp

        while curr.next:
            if curr.next.val != val:
                curr = curr.next

            else:
                curr.next = curr.next.next

        return temp.next