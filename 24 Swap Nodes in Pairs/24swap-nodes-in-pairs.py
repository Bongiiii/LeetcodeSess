# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case, no head or no next
        if not head or not head.next:
            return head

        #take 2 to swap and begin after the 2 which is 3rd
        swapper = self.swapPairs(head.next.next)

        temp = head.next
        temp.next = head
        head.next = swapper

        return temp

